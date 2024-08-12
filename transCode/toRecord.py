import pandas as pd
from datetime import datetime
import re


def extractDate(date):
    dt = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')

    return dt.year, dt.month

def extractLoc(locality):
    #print(locality)
    if locality == 'unknown' or locality == 'County' or locality == 'Taiwan':
        county = township = None
    else:
        pattern1 = r"(.*?[縣市])(.*)"
        pattern2 = r"(.*?[鄉鎮市區])(.*)"

        match1 = re.match(pattern1, locality)
        county = match1.group(1)
        township = re.match(pattern2, match1.group(2)).group(1) if match1.group(2) else None
 
        return  county, township


df = pd.read_csv('inputData/麻雀.csv')


# 把'standardOrganismQuantity'為0的刪掉
df = df[df['standardOrganismQuantity'] != 0]
record = df[['id', 'standardLongitude', 'standardLatitude', 'standardOrganismQuantity', 'taxonID']].copy()
record['standardOrganismQuantity'] = record['standardOrganismQuantity'].fillna(1)
record[['year', 'month']] = df['standardDate'].apply(lambda x: pd.Series(extractDate(x)))
record[['county','township']] = df['locality'].apply(lambda x: pd.Series(extractLoc(x)))

# 統一「臺」寫法
tai_dict = {'台北市': '臺北市', '台中市': '臺中市', '台東縣': '臺東縣', '台南市': '臺南市'}
record['county'] = record['county'].replace(tai_dict)

new_order = ['id', 'year', 'month', 'county','township']
record = record[new_order + [col for col in record.columns if col not in new_order]]
record = record.rename(columns={'standardLongitude': 'longitude', 'standardLatitude': 'latitude', 'standardOrganismQuantity': 'quantity'})


species = df[['taxonID', 'scientificName', 'common_name_c', 'kingdom_c', 'phylum_c', 'class_c', 'order_c', 'family_c', 'genus_c']].copy()
species = species.drop_duplicates()


# Save to .csv files.
record.to_csv('finalData/record_birds.csv', index=False)
species.to_csv('finalData/species.csv', index=False)