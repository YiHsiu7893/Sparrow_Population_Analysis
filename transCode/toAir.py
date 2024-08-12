import pandas as pd
import csv


data = ['siteID', 'year', 'month', '溫度', '相對濕度', '風速', '小時風速值', '降雨強度', '導電度', '氮氧化物', '懸浮微粒', '細懸浮微粒', '二氧化硫', '二氧化氮', '一氧化氮', '二氧化碳', '一氧化碳', '臭氧', '非甲烷碳氫化合物', '甲烷', '總碳氫化物', '酸雨', '總碳氫化合物']
dict = {'溫度' : 3, '相對濕度' : 4, '風速' : 5, '小時風速值' : 6, '降雨強度' : 7,
        '導電度' : 8, '氮氧化物' : 9, '懸浮微粒' : 10, '細懸浮微粒' : 11, '二氧化硫' : 12,
        '二氧化氮' : 13, '一氧化氮' : 14, '二氧化碳' : 15, '一氧化碳' : 16, '臭氧' : 17,
        '非甲烷碳氫化合物' : 18, '甲烷' : 19, '總碳氫化物' : 20, '酸雨' : 21, '總碳氫化合物' : 22}


df = pd.read_csv('inputData/air.csv', encoding='utf-8') 


current = None
with open('finalData/air.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)

    for index, row in df.iterrows():
        if (row['siteid'], row['monitormonth']) != current:
            csvwriter.writerow(data)

            current = (row['siteid'], row['monitormonth'])

            data = [None] * 23
            data[0] = row['siteid']
            data[1] = row['year']
            data[2] = row['month']

        data[dict[row['itemname']]] = row['concentration']
