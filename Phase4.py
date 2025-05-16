import pandas as pd

import matplotlib.pyplot as plt

# Load CSV data

df = pd.read_csv('global-data-on-sustainable-energy.csv')

# Filter data for Afghanistan (2000-2005)

df_afghanistan = df[(df['Entity'] == 'Afghanistan') & (df['Year'] >= 2000) & (df['Year'] <= 

2005)]

# Bar Chart: Access to electricity

plt.figure()

plt.bar(df_afghanistan['Year'], df_afghanistan['Access to electricity (% of population)'], 

color='red')

plt.title('Access to Electricity (2000-2005)')

plt.xlabel('Year')

plt.ylabel('% of Population')

plt.savefig('bar_chart.png')

# Scatter Plot: GDP per capita vs Access to electricity

plt.figure()

plt.scatter(df_afghanistan['gdp_per_capita'], df_afghanistan['Access to electricity (% of 

population)'])

plt.title('GDP vs Electricity Access')

plt.xlabel('GDP per Capita')

plt.ylabel('Access to Electricity (%)')

plt.savefig('scatter_plot.png')
