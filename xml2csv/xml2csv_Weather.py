import xml.etree.ElementTree as ET
import csv
import os


def transDate(date):
    stddate = date.split('-')

    standardDate = stddate[0] + '/' + stddate[1]
    if len(stddate) == 3:
        standardDate = standardDate + '/' + stddate[2]

    return standardDate


# 解析XML文件
tree = ET.parse('weather/mn_Report_201501.xml')
root = tree.getroot()
namespaces = {'cwa': 'urn:cwa:gov:tw:cwacommon:0.1'}

metadata = []    
elements = root.findall('.//cwa:resources/cwa:resource/cwa:metadata/cwa:statistics/cwa:weatherElements/cwa:weatherElement', namespaces)
for element in elements:
    tag = element.find('cwa:tagName', namespaces).text
    #print(tag)

    methods = element.findall('cwa:statisticalMethods/cwa:statisticalMethod/cwa:methodTagName', namespaces)
    methods_list = [method.text for method in methods]
    #print(methods_list)

    descriptions = element.findall('cwa:statisticalMethods/cwa:statisticalMethod/cwa:description', namespaces)
    description_list = [description.text for description in descriptions]
    #print(description_list, '\n')

    metadata.append((tag, methods_list, description_list))

headers = ['觀測站ID', '觀測站', '時間']
for m in metadata:
    for cm in m[2]:
        headers.append(cm)


with open('../inputData/weather.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerow(headers)

    for filename in os.listdir('weather'):
        file_path = os.path.join('weather', filename)
        
        tree = ET.parse(file_path)
        root = tree.getroot()

        locations = root.findall('.//cwa:resources/cwa:resource/cwa:data/cwa:surfaceObs/cwa:location', namespaces)
        for location in locations:
            data = []
            stationID = location.find('cwa:station/cwa:StationID', namespaces).text
            stationName = location.find('cwa:station/cwa:StationName', namespaces).text
            #print([stationID, stationName])

            statistics = location.find('cwa:stationObsStatistics', namespaces)
            date = transDate(statistics.find('cwa:YearMonth', namespaces).text)
            #print(date)

            data.extend([stationID, stationName, date])

            for header in metadata:
                for item in header[1]:
                    tag = statistics.find(f'cwa:{header[0]}/cwa:monthly/cwa:{item}', namespaces).text
                    if 'Date' in item:
                        if tag:
                            tag = transDate(tag)
                    #print(tag)
                    data.append(tag)

            csvwriter.writerow(data)