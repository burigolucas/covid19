# Retrieve reported cases of COVID19
import requests
import pandas as pd
import numpy as np

alpha2Code = []
name = []
total = []
death = []
recov = []

query = 'https://api.covid19api.com/summary'
response = requests.get(query)
if response.status_code != 200:
    raise "Error in retrieving data from API"
data = response.json()

for country in data['Countries']:

    name.append(country['Country'])
    alpha2Code.append(country['CountryCode'])
    total.append(country['TotalConfirmed'])
    death.append(country['TotalDeaths'])
    recov.append(country['TotalRecovered'])

df = pd.DataFrame(data={'Country':   name,
                        'alpha2Code': alpha2Code,
                        'Covid19_total':     total,
                        'Covid19_deaths':    death,
                        'Covid19_recovered': recov})

df['Covid19_active'] = df['Covid19_total']-df['Covid19_recovered']
df['Covid19_fatality'] = df['Covid19_deaths']/df['Covid19_total']
df.sort_values(by='Covid19_total',ascending=False,inplace=True)
df = df.reset_index(drop=True)
print("Top-10 countries by total reported COVID-19 cases")
print(df.head(10))

df.to_csv('data_COVID19.csv',index=False)