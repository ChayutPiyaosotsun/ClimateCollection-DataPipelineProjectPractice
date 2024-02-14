import matplotlib.pyplot as plt
from matplotlib import style
from sqlalchemy import func, extract
from database.models import Session, ProcessedWeatherData
from datetime import datetime
import os

plt.style.use('fivethirtyeight')

def plot_monthly_temperature_trends(city_name):
    session = Session()
    monthly_avg_temps = session.query(
        extract('month', ProcessedWeatherData.datetime).label('month'),
        func.avg(ProcessedWeatherData.temperature).label('average_temperature')
    ).filter(ProcessedWeatherData.city_name == city_name).group_by('month').all()

    avg_months = [month for month, _ in monthly_avg_temps]
    avg_temps = [temp for _, temp in monthly_avg_temps]

    plt.figure(figsize=(10, 6))
    plt.plot(avg_months, avg_temps, marker='o', linestyle='-', color='b')
    plt.xlabel('Month')
    plt.ylabel('Average Temperature (°C)')
    plt.title(f'Average Monthly Temperature for {city_name}')
    plt.xticks(avg_months, [datetime(2023, month, 1).strftime('%B') for month in avg_months], rotation=45)
    plt.tight_layout()
    plt.savefig(f'graphs/{city_name}_monthly_trend.png')
    plt.close()

    session = Session()
    monthly_data = session.query(
        extract('month', ProcessedWeatherData.datetime).label('month'),
        ProcessedWeatherData.temperature
    ).filter(ProcessedWeatherData.city_name == city_name).all()

    # Prepare data for plotting
    months = [datetime(2023, month, 1).strftime('%B') for month, _ in monthly_data]
    temperatures = [temp for _, temp in monthly_data]

    # Histogram for temperature distribution
    plt.figure(figsize=(10, 6))
    plt.hist(temperatures, bins=12, color='skyblue')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    plt.title(f'Histogram - Temperature Distribution for {city_name}')
    plt.tight_layout()
    plt.savefig(f'graphs/{city_name}_histogram.png')
    plt.close()

    # Boxplot for temperature spread
    plt.figure(figsize=(10, 6))
    plt.boxplot(temperatures)
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Boxplot - Temperature Spread for {city_name}')
    plt.xticks([1], [city_name])
    plt.tight_layout()
    plt.savefig(f'graphs/{city_name}_boxplot.png')
    plt.close()
    
    # Scatter plot for individual temperature points over time
    plt.figure(figsize=(10, 6))
    plt.scatter(months, temperatures, color='b')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Scatter Plot - Monthly Temperature for {city_name}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'graphs/{city_name}_scatter_plot.png')
    plt.close()

if __name__ == "__main__":
    # Ensure the 'graphs' directory exists
    if not os.path.exists('graphs'):
        os.makedirs('graphs')

    cities = ["Bangkok,TH", "Phetchaburi,TH", "TAK,TH", "Surat Thani,TH", "Ratchaburi,TH", "Phuket,TH", "Nakhon Si Thammarat,TH", "Chiang Rai,TH"]
    for city in cities:
        plot_monthly_temperature_trends(city)

