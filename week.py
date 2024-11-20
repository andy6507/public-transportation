import pandas as pd
import matplotlib.pyplot as plt

file_path = "교통이용통계.csv"
df = pd.read_csv(file_path, encoding='cp949')


df['가장 높은 요일'] = df[['일요일(휴일포함)', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']].idxmax(axis=1)


weekdays = ['일요일(휴일포함)', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']


weekday_counts = df['가장 높은 요일'].value_counts().reindex(weekdays, fill_value=0)


plt.figure(figsize=(10, 6))
weekday_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('요일별 가장 높은 요일 개수')
plt.xlabel('요일')
plt.ylabel('개수')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df[['년도', '월', '도로명', '가장 높은 요일']]
