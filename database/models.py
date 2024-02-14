from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class RawWeatherData(Base):
    __tablename__ = 'raw_weather_data'
    id = Column(Integer, primary_key=True)
    city = Column(String, index=True)
    data = Column(Text)
    datetime = Column(DateTime, default=func.now())

class ProcessedWeatherData(Base):
    __tablename__ = 'processed_weather_data'
    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, index=True)
    city_name = Column(String, index=True)
    temperature = Column(Float)
    humidity = Column(Integer)
    wind_speed = Column(Float)
    description = Column(String)
    datetime = Column(DateTime, default=func.now())

if not os.path.exists('data'):
    os.mkdir('data')

engine = create_engine('sqlite:///data/weather_data.db')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
