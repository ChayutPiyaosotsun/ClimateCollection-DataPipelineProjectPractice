import requests
import json
import sys
import os
from database.models import RawWeatherData, Session
from datetime import datetime, timedelta
from dotenv import load_dotenv

def fetch_historical_weather(api_key, start, end, city):
    url = f"https://history.openweathermap.org/data/2.5/history/city?q={city}&type=hour&start={start}&end={end}&appid={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def collect_data_for_2023(api_key, city):
    session = Session()
    # Check the last entry for this city in the database
    last_entry = session.query(RawWeatherData).filter(RawWeatherData.city == city).order_by(RawWeatherData.datetime.desc()).first()
    
    # If there's an entry, convert its datetime to a Unix timestamp and use it as the start; otherwise, use the start of 2023
    start_timestamp = str(int(last_entry.datetime.timestamp()) + 1) if last_entry else "1688169600"
    # Your end timestamp seems to be fixed for 2023, adjust if necessary
    end_timestamp = "1704067199"
    
    weather_data = fetch_historical_weather(api_key, start_timestamp, end_timestamp, city)
    if weather_data:
        store_raw_weather_data(city, weather_data)
    else:
        print(f"Error fetching data for {city}")

def store_raw_weather_data(city, raw_data):
    session = Session()
    # Assume 'dt' is the last epoch timestamp in the fetched data
    last_timestamp = raw_data['list'][-1]['dt']
    
    # Convert the Unix timestamp to a datetime object for storage
    last_datetime = datetime.utcfromtimestamp(last_timestamp)
    
    # Store the new data with the converted datetime object
    raw_entry = RawWeatherData(city=city, data=json.dumps(raw_data), datetime=last_datetime)
    session.add(raw_entry)
    session.commit()
    # if last_timestamp != "1704067199":
    #     collect_data_for_2023(api_key, city)
    print(f"Data stored for {city} up until epoch {last_timestamp}")

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
    cities = ['Bangkok,TH', 'Phetchaburi,TH', 'TAK,TH', 'Surat Thani,TH', 'Ratchaburi,TH', 'Phuket,TH', 'Nakhon Si Thammarat,TH', 'Chiang Rai,TH']
    for city in cities:
        collect_data_for_2023(api_key, city)

