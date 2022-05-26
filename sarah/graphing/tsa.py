import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt

# Pandas test to reformat TSA passenger data into a more usable format.

# impersonate headers to avoid 403 error
# TSA official passenger data
tsa_url = 'https://www.tsa.gov/coronavirus/passenger-throughput'
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(tsa_url, headers=header)

table_tsa =  pd.read_html(r.text)

print(f'Total tables: {len(table_tsa)}')

df = table_tsa[0]

# strip the year so it's easier to do comparisons
df['Date'] = df['Date'].astype('datetime64').dt.strftime('%m/%d')
df['2022'].astype('float64')

# can move this into data formatting during the read_html() call?
df['2021'].astype('float64')
df['2020'].astype('float64')
df['2019'].astype('float64')

df.sort_values(by='Date',inplace=True)

plt.style.use('seaborn-whitegrid')
df.plot.line(x='Date', y=['2019','2020','2021','2022'])
plt.title('TSA Passenger Data (2019 : no COVID-19)')
plt.xlabel('Day of Year')
plt.ylabel('Passengers (Millions)')
plt.show()
