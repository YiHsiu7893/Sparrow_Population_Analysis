import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import MinMaxScaler


# Change to the element to be analyzed.
df = pd.read_csv('finalData/riverAna.csv', encoding='big5') 
element = 'O2'


# Filter out unique and valid siteIDs.
unique_ids = df['siteID'].unique()
rows_with_empty_values = df[df[element].isna()]
empty_value_ids = rows_with_empty_values['siteID'].unique()
valid_ids = [id for id in unique_ids if id not in empty_value_ids]

df = df[~df['siteID'].isin(empty_value_ids)]

# The upper and lower bounds of all '生物數量' and the specified element.
c_l = df['生物數量'].min()
c_u = df['生物數量'].max()
v_l = df[element].min()
v_u = df[element].max()
# Set the scalers for data normalization.
scaler1 = MinMaxScaler(feature_range=(c_l, c_u))
scaler2 = MinMaxScaler(feature_range=(v_l, v_u))


creature = []
value = []
for id in valid_ids:
    data = df[df['siteID'] == id]

    # At least 5 data points are required for reliability.
    if len(data) < 5:
        continue

    # Normalize and append.
    creature.append(scaler1.fit_transform(data['生物數量'].values.reshape(-1, 1)))
    value.append(scaler2.fit_transform(data[element].values.reshape(-1, 1)))

creature = np.concatenate([c.flatten() for c in creature])
value = np.concatenate([v.flatten() for v in value])


# Analysis
# (optional) Spearman rank-order correlation coefficient.
score, p = spearmanr(creature, value)
print("Spearman相關係數: {:.2f}".format(score))
print("P值: {:.2e}".format(p))
if p >= 0.05:
    print("相關性不顯著")
else:
    print("相關性顯著")

# (optional) Scatter plot of the specified monitoring station.
data = df[df['siteID'] == '1017']

plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['生物數量'], y=data[element], marker='D', s=100, color='saddlebrown')
plt.xticks([])
plt.yticks([])

plt.show()