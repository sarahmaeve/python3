import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt

def main():
    # TSA official passenger data
    tsa_url = 'https://www.tsa.gov/coronavirus/passenger-throughput'
    header = {
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
      "X-Requested-With": "XMLHttpRequest"
    }

    r = requests.get(tsa_url, headers=header)

    table_tsa = pd.read_html(r.text)

    print(f'Total tables: {len(table_tsa)}')

    df = table_tsa[0]

    # strip the year so it's easier to do comparisons
    df['Date'] = df['Date'].astype('datetime64').dt.strftime('%m/%d')
    df['2023'] = df['2023'].astype('float64')
    df['2022'] = df['2022'].astype('float64')
    df['2021'] = df['2021'].astype('float64')
    df['2020'] = df['2020'].astype('float64')
    df['2019'] = df['2019'].astype('float64')

    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)

    plot_tsa_data(df)

def plot_tsa_data(df):
    plt.style.use('seaborn-v0_8-whitegrid')
    df.plot.line(y=['2019', '2020', '2021', '2022','2023'])
    plt.title('TSA Passenger Data (2019: no COVID-19)')
    plt.xlabel('Day of Year')
    plt.ylabel('Passengers (Millions)')
    plt.show()

if __name__ == "__main__":
    main()

