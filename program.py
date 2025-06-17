import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read train.csv
train_df = pd.read_csv('datasets/train.csv')

cluster_1 = train_df[train_df['cluster_id'] == 'cluster_1']
cluster_2 = train_df[train_df['cluster_id'] == 'cluster_2']
cluster_3 = train_df[train_df['cluster_id'] == 'cluster_3']
cluster_4 = train_df[train_df['cluster_id'] == 'cluster_4']

cluster_1['date'] = pd.to_datetime(cluster_1['date'])
plt.figure(figsize=(10, 5))
#plt.plot(cluster_1['date'], cluster_1['temperature_2m_max'],color='r')
#plt.plot(cluster_1['date'], cluster_1['temperature_2m_min'],color='g')
#plt.xlabel('Date')
#plt.ylabel('Temperature in Celsius')
#plt.title('Temperature Maximum and Minimum Over Time for Cluster 1')
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()

cluster_1['daylight_duration'] = cluster_1['daylight_duration'] / 3600
plt.plot(cluster_1['date'], cluster_1['daylight_duration'], color = 'b')
plt.xlabel('Date')
plt.ylabel('Daylight Duration')
plt.title('Daylight Duration Over Time for Cluster 1')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# All columns inside the train.csv:
#        'ID', 'date', 'cluster_id', 'electricity_consumption',
#       'temperature_2m_max', 'temperature_2m_min', 'apparent_temperature_max',
#       'apparent_temperature_min', 'sunshine_duration', 'daylight_duration',
#       'wind_speed_10m_max', 'wind_gusts_10m_max',
#       'wind_direction_10m_dominant', 'shortwave_radiation_sum',
#       'et0_fao_evapotranspiration'

# Target column: electricity_consumption

# Goal: use the other column data to find the electricity_consumption


# Write to submission.csv (example: create an empty DataFrame and save)
#submission_df = pd.DataFrame()  # Replace with your submission data

# Do this only when submitting the data.
#submission_df.to_csv('submission.csv', index=False)

# Read from submission.csv
#submission_read = pd.read_csv('submission.csv')