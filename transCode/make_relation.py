import pandas as pd
from geopy.distance import geodesic


# func: Compute distance and find the nearest monitoring station.
def distance(long, lat):
    min_dist = float('inf')
    min_id = None
    point = (lat, long)

    for _, row in station.iterrows():
        loc = (row['latitude'], row['longitude'])

        dist = geodesic(loc, point).kilometers
        if dist < min_dist:
            min_dist = dist
            min_id = row['siteID']
    
    return min_id
    

station = pd.read_csv('finalData/riverStation.csv', encoding='big5', encoding_errors='ignore')

record = pd.read_csv('finalData/record.csv', encoding='big5', encoding_errors='ignore')
df = record[['longitude', 'latitude']].drop_duplicates()
df = df.dropna()
df['siteID'] = df.apply(lambda row: distance(row['longitude'], row['latitude']), axis=1)

df.to_csv('finalData/RecordRiver.csv', index=False)