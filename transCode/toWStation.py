import pandas as pd
import re


def extractRegion(address):
    pattern = r"(.*?[鄉鎮市區])(.*)"

    match = re.match(pattern, address)
    
    return match.group(1)


df = pd.read_csv('inputData/氣象測站基本資料.csv', encoding='big5')

df = df[df['status'].str.contains('現存測站')]
df['township'] = df['Location'].apply(extractRegion)
df = df[['StationID', 'StationName', 'CountyName', 'township', 'StationLongitude', 'StationLatitude']]
df = df.rename(columns={'StationID': 'siteID', 'StationName': 'siteName', 'CountyName': 'county', 'StationLongitude': 'longitude', 'StationLatitude': 'latitude'})

df.to_csv('finalData/weatherStation.csv', index=False)