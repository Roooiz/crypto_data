from datetime import date
import pandas as pd

print("-------COINGECKO_DATA_ANALYSIS------\n")

path1 = input("Введите путь к первому файлу: ")
path2 = input("Введите путь ко второму файлу: ")

print("Подготовка первого файла")
data1 = pd.read_csv(path1)
df1 = pd.DataFrame(data1)
dt1 = df1[['#', 'Coin']]
sort_dt1 = dt1.sort_values('Coin')
sort_dt1.reset_index(drop=True, inplace=True)

print("Подготовка второго файла")
data2 = pd.read_csv(path2)
df2 = pd.DataFrame(data2)
dt2 = df2[['#', 'Coin']]
sort_dt2 = dt2.sort_values('Coin')
sort_dt2.reset_index(drop=True, inplace=True)

cut_sort_dt1 = sort_dt1[sort_dt1.Coin.isin(sort_dt2.Coin)]
cut_sort_dt2 = sort_dt2[sort_dt2.Coin.isin(sort_dt1.Coin)]

cut_sort_dt1.reset_index(drop=True, inplace=True)
cut_sort_dt2.reset_index(drop=True, inplace=True)

print("Формирование таблицы")
cut_sort_dt1.rename(columns={'#': 'before'}, inplace=True)
cut_sort_dt2.rename(columns={'#': 'after'}, inplace=True)

sort_dt = cut_sort_dt1
sort_dt = sort_dt.join(cut_sort_dt2['after'])
sort_dt['result'] = sort_dt['before'] - sort_dt['after']

final_data = sort_dt.sort_values('result', ascending=False)
final_data.reset_index(drop=True, inplace=True)

current_date = date.today()

final_data.to_csv(f'Result_crypto_analysis_{current_date}.csv', index=False)
print(f"Работа завершена.\n\nЗагруженный файл: Result_crypto_analysis_{current_date}.csv")
