# Description

In this project, the case fatality rate (CFR) for the COVID-19 outbreak is analysed to answer the following questions:

- **Q1** What is the case fatality rate (CFR) of COVID-19?
- **Q2** Is there a significant variation of CFR for COVID-19 among different countries?
- **Q3** What country-specific features might affect the case fatality rate?

As for April 28th 2020, the analysis of the data reveals that: 

**A1** The average case fatality rate (CFR) for COVID-19 for the 35 countries with number of reported cases above 10,000 (as for 28th April 2020) was observed to be 5.4%.

**A2** The average CFR is highly affected by the quality of the reports from each country. For a few cases (e.g., Russia), the reported deaths are likely undereported. A significant variation of CFR among countries is observed. In particular, 7 countries were observed to have a CFR above 10% with the highest value of 15.4% for Belgian. All the 7 countries with CFR above 10% are European and this values is significantly differenet from Germany, which is among the top-5 affect countris as per number of reported cases.

**A3** To consider for possible country-specific features affecting the case fatality rate, the correlation of health indicators with CFR was calculated. In particular, the results suggest that health indicators like number of hospital beds and physicians could explain why Germany is coping with the COVID-19 outbread significantly better than its neighbor countries.

Only aggregated data were considered in the analysis, without taking into account the time evolution of the active cases. Further relevant aspects which need to be also account are the impact of the timeline of number of active cases as well as the effect of number of tests performed.

## Methodology

The analysis is all structured in the Jupyter notebook `COVID19.ipynb`. API's requests are used to pull updated data on COVID-19 outbreak as well as data for several indiators from WorldBank and OECD.

## Library dependencies

- requests
- pandas
- numpy
- matplotlib


## Resources

Data is collected using a range of API's, including:

- https://api.covid19api.com/
- https://restcountries.eu/
- https://corona-api.com
- http://api.worldbank.org
- https://stats.oecd.org/