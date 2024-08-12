import xml.etree.ElementTree as ET
import csv


# 解析XML文件
tree = ET.parse('Station.xml')
root = tree.getroot()
namespaces = {'cwa': 'urn:cwa:gov:tw:cwacommon:0.1'}

headers = []    
fields = root.findall('.//cwa:resources/cwa:resource/cwa:metadata/cwa:fields/cwa:field', namespaces)
for field in fields:
    tag = field.find('cwa:tagName', namespaces).text
    
    #if tag != 'Notes':
    headers.append(tag)


with open('../inputData/氣象測站基本資料.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerow(headers)

    stations = root.findall('.//cwa:resources/cwa:resource/cwa:data/cwa:stationsStatus/cwa:station', namespaces)
    for station in stations:
        data = []
        for h in headers:
            tag = station.find(f'cwa:{h}', namespaces).text
            data.append(tag)

        csvwriter.writerow(data)