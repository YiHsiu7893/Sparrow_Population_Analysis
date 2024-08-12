import pandas as pd

df = pd.read_csv('inputData/river.csv')
df = df.drop(columns=['測站名稱', '採樣分區', '河川', '縣市', '水體分類等級', '採樣日期', '採樣時間', '備註'])

first_col = '測站編號'
df = df[[first_col] + [col for col in df.columns if col != first_col]]
df = df.rename(columns={'測站編號': 'siteID', '採樣年': 'year', '採樣月': 'month'})

df = df.replace("--", None)

df.to_csv('finalData/river.csv', index=False)