from datetime import date
import requests
from bs4 import BeautifulSoup
import pandas as pd

print("-------COINGECKO_DATA_DOWNLOAD------\n")

current_date = date.today()
tables = []

for i in range(1, 31):
    url = f'https://www.coingecko.com/?locale=en&page={i}'
    print(f'Загрузка {i} страницы')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables.append(pd.read_html(str(soup))[0])

master_table = pd.concat(tables)
master_table = master_table.loc[:, master_table.columns[1:-1]]

master_table.to_csv(f'Crypto_Data_{current_date}.csv', index=False)
print(f"\nРабота завершена.\n\nРезультат в файле: Crypto_Data_{current_date}.csv")
