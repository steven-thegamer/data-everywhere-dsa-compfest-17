import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def compare_electricity_consumption():
    # Load the CSV data
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])

    # Create a pivot table for better plotting
    pivot_df = df.pivot(index='date', columns='cluster_id', values='electricity_consumption')

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Plot each cluster's electricity consumption
    for cluster in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[cluster], label=cluster, marker='o', markersize=4)

    # Configure plot settings
    plt.title('Electricity Consumption by Cluster', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Electricity Consumption', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Cluster ID')
    # Format x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()  # Rotate date labels

    plt.tight_layout()
    plt.show()

def compare_max_temperature():
    # Load the CSV data
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])

    # Create a pivot table for better plotting
    pivot_df = df.pivot(index='date', columns='cluster_id', values='temperature_2m_max')

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Plot each cluster's temperature
    for cluster in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[cluster], label=cluster, marker='o', markersize=4)

    # Configure plot settings
    plt.title('Max Temperature by Cluster', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Cluster ID')
    # Format x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()  # Rotate date labels

    plt.tight_layout()
    plt.show()

def compare_min_temperature():
    # Load the CSV data
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])

    # Create a pivot table for better plotting
    pivot_df = df.pivot(index='date', columns='cluster_id', values='temperature_2m_min')

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Plot each cluster's temperature
    for cluster in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[cluster], label=cluster, marker='o', markersize=4)

    # Configure plot settings
    plt.title('Min Temperature by Cluster', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Cluster ID')
    # Format x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()  # Rotate date labels

    plt.tight_layout()
    plt.show()

def compare_max_apparent_temperature():
    # Load the CSV data
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])

    # Create a pivot table for better plotting
    pivot_df = df.pivot(index='date', columns='cluster_id', values='apparent_temperature_max')

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Plot each cluster's apparent temperature
    for cluster in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[cluster], label=cluster, marker='o', markersize=4)

    # Configure plot settings
    plt.title('Max Apparent Temperature by Cluster', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Apparent Temperature (°C)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Cluster ID')
    # Format x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()  # Rotate date labels

    plt.tight_layout()
    plt.show()

def compare_min_apparent_temperature():
    # Load the CSV data
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])

    # Create a pivot table for better plotting
    pivot_df = df.pivot(index='date', columns='cluster_id', values='apparent_temperature_min')

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Plot each cluster's apparent temperature
    for cluster in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[cluster], label=cluster, marker='o', markersize=4)

    # Configure plot settings
    plt.title('Min Apparent Temperature by Cluster', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Apparent Temperature (°C)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Cluster ID')
    # Format x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()  # Rotate date labels

    plt.tight_layout()
    plt.show()

def compare_sunshine_duration():
    # Load the CSV data
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])

    # Create a pivot table for better plotting
    pivot_df = df.pivot(index='date', columns='cluster_id', values='sunshine_duration')

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Plot each cluster's apparent temperature
    for cluster in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[cluster], label=cluster, marker='o', markersize=4)

    # Configure plot settings
    plt.title('Sunshine Duration by Cluster', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Sunshine Duration', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Cluster ID')
    # Format x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()  # Rotate date labels

    plt.tight_layout()
    plt.show()

def compare_daylight_duration():
    # Load the CSV data
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])

    # Create a pivot table for better plotting
    pivot_df = df.pivot(index='date', columns='cluster_id', values='daylight_duration')

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Plot each cluster's apparent temperature
    for cluster in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[cluster], label=cluster, marker='o', markersize=4)

    # Configure plot settings
    plt.title('Daylight Duration by Cluster', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Daylight Duration', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Cluster ID')
    # Format x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()  # Rotate date labels

    plt.tight_layout()
    plt.show()

def compare_wind_speed_10m_max():
    # Load the CSV data
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])

    # Create a pivot table for better plotting
    pivot_df = df.pivot(index='date', columns='cluster_id', values='wind_speed_10m_max')

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Plot each cluster's apparent temperature
    for cluster in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[cluster], label=cluster, marker='o', markersize=4)

    # Configure plot settings
    plt.title('Wind Speed in 10 m by Cluster', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Wind Speed (m/s)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Cluster ID')
    # Format x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()  # Rotate date labels

    plt.tight_layout()
    plt.show()

def compare_shortwave_radiation_sum():
    # Load the CSV data
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])

    # Create a pivot table for better plotting
    pivot_df = df.pivot(index='date', columns='cluster_id', values='shortwave_radiation_sum')

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Plot each cluster's apparent temperature
    for cluster in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[cluster], label=cluster, marker='o', markersize=4)

    # Configure plot settings
    plt.title('Shortwave Radiation by Cluster', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Shortwave Radiation', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Cluster ID')
    # Format x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()  # Rotate date labels

    plt.tight_layout()
    plt.show()

def compare_wind_gusts_10m_max():
    # Load the CSV data
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])

    # Create a pivot table for better plotting
    pivot_df = df.pivot(index='date', columns='cluster_id', values='wind_gusts_10m_max')

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Plot each cluster's apparent temperature
    for cluster in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[cluster], label=cluster, marker='o', markersize=4)

    # Configure plot settings
    plt.title('Wind Gusts in 10 m by Cluster', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Wind Gusts (m/s)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Cluster ID')
    # Format x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()  # Rotate date labels

    plt.tight_layout()
    plt.show()

def compare_wind_direction_10m_dominant():
    # Load the CSV data
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])

    # Create a pivot table for better plotting
    pivot_df = df.pivot(index='date', columns='cluster_id', values='wind_direction_10m_dominant')

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Plot each cluster's apparent temperature
    for cluster in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[cluster], label=cluster, marker='o', markersize=4)

    # Configure plot settings
    plt.title('Wind Direction by Cluster', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Wind Direction', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Cluster ID')
    # Format x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()  # Rotate date labels

    plt.tight_layout()
    plt.show()

def compare_et0_fao_evapotranspiration():
    # Load the CSV data
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])

    # Create a pivot table for better plotting
    pivot_df = df.pivot(index='date', columns='cluster_id', values='et0_fao_evapotranspiration')

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Plot each cluster's apparent temperature
    for cluster in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[cluster], label=cluster, marker='o', markersize=4)

    # Configure plot settings
    plt.title('Evaporation by Cluster', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Evaporation', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Cluster ID')
    # Format x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()  # Rotate date labels

    plt.tight_layout()
    plt.show()

def compare_energy_consumption_vs_daylight_duration():
    # Load the CSV data
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])

    # Group by cluster_id and sum energy consumption and daylight duration
    grouped = df.groupby('cluster_id').agg({
        'electricity_consumption': 'sum',
        'daylight_duration': 'sum'
    })

    # Plot
    plt.figure(figsize=(10, 7))
    plt.scatter(grouped['daylight_duration'], grouped['electricity_consumption'], s=100)

    # Annotate each point with cluster_id
    for cluster_id, row in grouped.iterrows():
        plt.annotate(str(cluster_id), (row['daylight_duration'], row['electricity_consumption']),
                     textcoords="offset points", xytext=(5,5), ha='left')

    plt.title('Total Electricity Consumption vs. Total Daylight Duration by Cluster', fontsize=14)
    plt.xlabel('Total Daylight Duration', fontsize=12)
    plt.ylabel('Total Electricity Consumption', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def compare_temperature_range():
    df = pd.read_csv('datasets/train.csv', parse_dates=['date'])
    df['temperature_2m_mean'] = (df['temperature_2m_max'] + df['temperature_2m_min']) / 2

    # Create a pivot table for better plotting
    pivot_df = df.pivot(index='date', columns='cluster_id', values='temperature_2m_mean')

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Plot each cluster's apparent temperature
    for cluster in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[cluster], label=cluster, marker='o', markersize=4)

    # Configure plot settings
    plt.title('Temperature Mean by Cluster', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Temperature Mean', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Cluster ID')
    # Format x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()  # Rotate date labels

    plt.tight_layout()
    plt.show()

compare_temperature_range()