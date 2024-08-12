import pandas as pd

df = pd.read_csv('inputData/weather.csv')
df = df.drop(columns=['觀測站', '時間', '最高溫度發生日期', '最低溫度發生日期', '最大10分鐘風發生日期', '最大10分鐘風風向', '最大瞬間風發生日期', '最大瞬間風風向', '最小相對濕度發生日期'])
df = df.rename(columns={'觀測站ID': 'siteID', '年': 'year', '月': 'month'})

# 將「累積降水量」為「T」的換成0
df['累積降水量'] = df['累積降水量'].replace('T', 0)
df['累積降水量'] = pd.to_numeric(df['累積降水量'], errors='coerce')
                        
df.to_csv('finalData/weather.csv', index=False)