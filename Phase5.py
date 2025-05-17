import pandas as pd

import matplotlib.pyplot as plt

# Load CSV file

df = pd.read_csv('2018Floor1.csv')

df['Date'] = pd.to_datetime(df['Date'])

# Prepare data

light_columns = ['z1_Light(kW)', 'z2_Light(kW)', 'z3_Light(kW)', 'z4_Light(kW)']

light_totals = df[light_columns].mean()

labels = light_totals.index

sizes = light_totals.values

time_series = df[['Date', 'z1_Light(kW)']]

# Plotting

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Pie chart

ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

ax1.set_title('Average Light Power Distribution')

# Line plot

ax2.plot(time_series['Date'], time_series['z1_Light(kW)'], color='red')

ax2.set_title('Zone 1 Light Power Over Time')

ax2.set_xlabel('Time')

ax2.set_ylabel('Power (kW)')

ax2.tick_params(axis='x', labelrotation=45)

plt.tight_layout()

plt.show()
