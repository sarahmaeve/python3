""" simple fetch and graph of TSA passenger data """
from datetime import datetime
import requests
import bs4 as bs
import matplotlib.pyplot as plt

source = requests.get('https://www.tsa.gov/coronavirus/passenger-throughput')
soup = bs.BeautifulSoup(source.text, features='lxml')
table = soup.table
chart_data = ()
dates = []
percentages = []

for tr in table.find_all('tr'):
    td = tr.find_all('td')
    row = [i.text for i in td]
    try:
        # check for blank final row[] and effectively ignore it
        if row and row[0] != 'Date':
            dates.append(datetime.strptime(row[0], '%m/%d/%Y'))
            percentages.append(int(row[1].replace(',', '')) / int(row[2].replace(',', '')))
    except IndexError:
        # just in case something is misformatted
        print(row)
        print("Processing stopped.")

y = percentages[::-1]
x = dates[::-1]
chart_data = (percentages[::-1])
plt.style.use('seaborn-dark')
plt.ylabel('Percentage of previous year passengers (TSA)')
# plt.plot(chart_data, linewidth=2.0)
plt.plot(x, y, linewidth=2.0)
plt.gcf().autofmt_xdate()
plt.title('Decline in Number of Airline Passengers in the COVID-19 Era')
plt.show()
