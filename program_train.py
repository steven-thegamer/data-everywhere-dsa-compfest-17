import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.calibration import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import seaborn as sns
from sklearn.model_selection import GridSearchCV

def plot_feature_importance(model, df):
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
        # Create feature importance dataframe
    importance_df = pd.DataFrame({
        'feature': df.columns,
        'importance': importances
    }).sort_values('importance', ascending=False)
    
    print("\nTop 15 Most Important Features:")
    print(importance_df.head(15))
    
    # Plot feature importance
    plt.figure(figsize=(12, 8))
    sns.barplot(data=importance_df.head(15), x='importance', y='feature')
    plt.title('Feature Importance (Random Forest)')
    plt.xlabel('Importance Score')
    plt.tight_layout()
    plt.show()
    return indices

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

def train_and_test(df):

    X = df.drop(columns=["electricity_consumption"])
    y = df["electricity_consumption"]

    X_train = X[(df["year"] >= 2013) & (df["year"] <= 2020)]
    y_train = y[(df["year"] >= 2013) & (df["year"] <= 2020)]

    X_test = X[(df["year"] >= 2021)]
    y_test = y[(df["year"] >= 2021)]

    X_train = X_train.drop(columns=["year"])
    X_test = X_test.drop(columns=["year"])

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predict using the trained model
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

    importances = model.feature_importances_
    feature_names = X_train.columns
    feature_importance_series = pd.Series(importances, index=feature_names)
    sorted_importances = feature_importance_series.sort_values(ascending=False)
    important_features = sorted_importances[sorted_importances > 0.005]
    print(sorted_importances)

def grid_search_tuning(X_train, y_train, X_test, y_test):
    param_grid = {
        'n_estimators': range(1700, 1900, 50),
        'max_depth': [20],
        'min_samples_split': [2],
    }

    grid_search = GridSearchCV(
        RandomForestRegressor(random_state=42),
        param_grid,
        cv=3,
        scoring='neg_mean_absolute_error',
        n_jobs=-1,
        verbose=1
    )

    grid_search.fit(X_train, y_train)

    print("Best parameters found:", grid_search.best_params_)
    best_model = grid_search.best_estimator_
    best_preds = best_model.predict(X_test)
    best_mae = mean_absolute_error(y_test, best_preds)
    best_rmse = np.sqrt(mean_squared_error(y_test, best_preds))
    print(f"Best Model MAE: {best_mae:.2f}")
    print(f"Best Model RMSE: {best_rmse:.2f}")

df = pd.read_csv("datasets/train.csv")
df = feature_engineering(df)
train_and_test(df)

# All columns inside the train.csv:
#        'ID', 'date', 'cluster_id', 'electricity_consumption',
#       'temperature_2m_max', 'temperature_2m_min', 'apparent_temperature_max',
#       'apparent_temperature_min', 'sunshine_duration', 'daylight_duration',
#       'wind_speed_10m_max', 'wind_gusts_10m_max',
#       'wind_direction_10m_dominant', 'shortwave_radiation_sum',
#       'et0_fao_evapotranspiration'

# Target column: electricity_consumption

# Goal: use the other column data to find the electricity_consumption