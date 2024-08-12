# 麻雀為何那樣? 探討影響麻雀數量的可能因素
### 第一屆 TBIA 生物開放資料數據松競賽, 2024
The goal is to use public data and analyze which factors might influence sparrow populations.  
Our conclusion is that agricultural land reduction and air pollution may affect sparrow numbers, while factors such as weather, river pollution, and predators could not be definitively assessed from the data.
## Database Schema
<img src="https://github.com/YiHsiu7893/Sparrow_Population_Analysis/blob/main/pictures/schema.png" width=80% height=60%>

## Data Description
| Item        | Description                                        |
|-------------|----------------------------------------------------|
| inputData   | cleaned data                                      |
| finalData   | transferred data                                  |
| pictures    | database schema and analysis results              |
| transCode   | codes performing data transformation              |
| xml2csv     | convert file format from XML to CSV, including Weather_Station and Weather |
| analysis.py | code performing Spearman correlation analysis     |
