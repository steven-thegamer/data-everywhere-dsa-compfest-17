import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load data
df = pd.read_csv("datasets/train.csv")
test_df = pd.read_csv("datasets/test.csv")

def feature_engineering(df):
    # Feature Engineering
    df["date"] = pd.to_datetime(df["date"])  # Re-add date temporarily
    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year

    # Seasonal features
    df['season'] = df['month'].map({12: 4, 1: 4, 2: 4,
                                    3: 1, 4: 1, 5: 1,
                                    6: 2, 7: 2, 8: 2,
                                    9: 3, 10: 3, 11: 3})

    df = df.drop(columns=["date"])

    df['temperature_2m_range'] = df['temperature_2m_max'] - df['temperature_2m_min']
    df['temperature_2m_mean'] = (df['temperature_2m_max'] + df['temperature_2m_min']) / 2
    df = df.drop(columns=["temperature_2m_max", "temperature_2m_min"])

    df['apparent_temperature_range'] = df['apparent_temperature_max'] - df['apparent_temperature_min']
    df['apparent_temperature_mean'] = (df['apparent_temperature_max'] + df['apparent_temperature_min']) / 2
    df = df.drop(columns=["apparent_temperature_max", "apparent_temperature_min"])
    # Drop unnecessary columns and wrong columns
    df = pd.get_dummies(df, columns=["cluster_id"], drop_first=False)
    df = df.drop(columns=["ID"])

    df = df.drop(columns=['wind_speed_10m_max','wind_gusts_10m_max','wind_direction_10m_dominant', 'sunshine_duration'])
    
    return df

df = feature_engineering(df)
test_df = feature_engineering(test_df)

X = df.drop(columns=["electricity_consumption"])
y = df["electricity_consumption"]

X_test = test_df

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Predict using the trained model
test_preds = model.predict(X_test)

submission_df = pd.read_csv("datasets/submission.csv")
submission_df["electricity_consumption"] = test_preds
submission_df.to_csv("submission.csv", index=False)

# All columns inside the train.csv:
#        'ID', 'date', 'cluster_id', 'electricity_consumption',
#       'temperature_2m_max', 'temperature_2m_min', 'apparent_temperature_max',
#       'apparent_temperature_min', 'sunshine_duration', 'daylight_duration',
#       'wind_speed_10m_max', 'wind_gusts_10m_max',
#       'wind_direction_10m_dominant', 'shortwave_radiation_sum',
#       'et0_fao_evapotranspiration'

# Target column: electricity_consumption

# Goal: use the other column data to find the electricity_consumption