import pandas as pd
import requests
import xml.etree.ElementTree as ET
import json


# func: land_query(long, lat)
def land_query(x, y, coord_code='4326'):
    # Combine API URL.
    url = f"https://api.nlsc.gov.tw/other/LandUsePointQuery/{x}/{y}/{coord_code}"
    
    response = requests.get(url)
    root = ET.fromstring(response.content)

    for item in root.findall('ITEM'):
        lname_c1 = item.find('Lname_C1').text
        lname_c2 = item.find('Lname_C2').text 
        name = item.find('NAME').text

    try:
        return lname_c1 #lname_c2, name
    except UnboundLocalError:
        return None

# func: alt_query(long, lat)
def alt_query(long, lat):
    url = url_root + str(lat) + "%2C" + str(long) + "&key=" + key
    #print(url)

    r = requests.get(url)
    #print(r.text)

    parsed = json.loads(r.text)
    alt = parsed["results"][0]["elevation"]
    #print(alt)
    
    return alt


if __name__ == "__main__":
    df = pd.read_csv('finalData/record.csv', encoding='latin1')
    df = df.dropna(subset=['latitude', 'longitude'])

    # Extract unique (long, lat) tuples.
    loc = df[['longitude', 'latitude']].drop_duplicates()

    # Add "Altitude" column, and call the "alt_query" function.
    url_root = "https://maps.googleapis.com/maps/api/elevation/json?locations="
    key = <my-google-api-key>
    loc['altitude'] = loc.apply(lambda row: alt_query(row['longitude'], row['latitude']), axis=1)

    # Add "landUse" column, and call the "land_query" function.
    loc['landUse'] = loc.apply(lambda row: land_query(row['longitude'], row['latitude']), axis=1)

    loc.to_csv('finalData/location.csv', index=False, encoding='utf-8', columns=['longitude', 'latitude', 'altitude', 'landUse'])