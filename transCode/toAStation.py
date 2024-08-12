import pandas as pd


df = pd.read_csv('inputData/空氣品質測站基本資料.csv')

df = df[['siteid', 'sitename', 'county', 'township', 'twd97lon', 'twd97lat']]
df = df.rename(columns={'siteid': 'siteID', 'sitename': 'siteName', 'twd97lon': 'longitude', 'twd97lat': 'latitude'})

df.to_csv('finalData/airStation.csv', index=False)