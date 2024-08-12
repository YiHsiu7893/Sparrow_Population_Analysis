import pandas as pd


df = pd.read_csv('inputData/河川水質測點基本資料.csv')

df = df[df['statusofuse'].str.contains('啟用')]
df = df[['siteid', 'sitename', 'county', 'township', 'twd97lon', 'twd97lat']]
df = df.rename(columns={'siteid': 'siteID', 'sitename': 'siteName', 'twd97lon': 'longitude', 'twd97lat': 'latitude'})
                        
df.to_csv('finalData/riverStation.csv', index=False)