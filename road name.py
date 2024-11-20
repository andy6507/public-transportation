import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

file_path = "교통이용통계.csv"

df = pd.read_csv(file_path, encoding='cp949')

df['가장 높은 요일'] = df[['일요일(휴일포함)', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']].idxmax(axis=1)

df['총 교통량'] = df[['일요일(휴일포함)', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']].sum(axis=1)

road_traffic = df.groupby('도로명')['총 교통량'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
road_traffic.plot(kind='bar', color='skyblue')

plt.title('도로별 교통량', fontsize=16)
plt.xlabel('도로명', fontsize=12)
plt.ylabel('총 교통량', fontsize=12)

plt.xticks(rotation=0, ha='center')  

plt.show()
