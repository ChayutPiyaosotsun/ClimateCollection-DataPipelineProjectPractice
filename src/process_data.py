from database.models import Session, RawWeatherData, ProcessedWeatherData
import json
from datetime import datetime

cities = [
    {"id": 1609350, "name": "Bangkok,TH"},
    {"id": 1149698, "name": "Phetchaburi,TH"},
    {"id": 1150490, "name": "TAK,TH"},
    {"id": 1150515, "name": "Surat Thani,TH"},
    {"id": 1150954, "name": "Ratchaburi,TH"},
    {"id": 1151254, "name": "Phuket,TH"},
    {"id": 1151933, "name": "Nakhon Si Thammarat,TH"},
    {"id": 1153669, "name": "Chiang Rai,TH"},
]

def process_and_store_weather_data():
    session = Session()
    raw_entries = session.query(RawWeatherData).all()

    for entry in raw_entries:
        data = json.loads(entry.data)
        city_name = entry.city  # Using the city name from the RawWeatherData entry
        city_info = next((city for city in cities if city["name"] == city_name), None)
        
        if not city_info:
            print(f"City name {city_name} not found in cities list.")
            continue
        
        for weather_entry in data['list']:
            weather_datetime = datetime.utcfromtimestamp(weather_entry['dt'])
            processed_entry = ProcessedWeatherData(
                city_id=city_info['id'],
                city_name=city_name,
                temperature=weather_entry['main']['temp'],
                humidity=weather_entry['main']['humidity'],
                wind_speed=weather_entry['wind']['speed'],
                description=weather_entry['weather'][0]['description'],
                datetime=weather_datetime
            )
            session.add(processed_entry)
    
    session.commit()
    print("Processed and stored all weather data.")

if __name__ == "__main__":
    process_and_store_weather_data()
