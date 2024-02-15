# ClimateCollection-DataPipelineProjectPractice

The Climate Collection Data Pipeline Project is an insightful data engineering initiative designed to fetch, process, analyze, and visualize weather data across multiple cities in Thailand. Utilizing OpenWeatherMap's historical data API, this project captures a wealth of climate-related information, such as temperature, humidity, and wind speeds.


## Features
- Data Collection: Automated scripts to fetch historical weather data for the year 2023.
- Data Processing: Transformation of raw weather data into a structured format suitable for analysis.
- Data Analysis: Python-based analysis tools to calculate average temperatures and other climate metrics.
- Data Visualization: Generation of compelling graphical representations of the analyzed data, including line graphs, histograms, and boxplots, providing clear visual insights into monthly and annual climate trends.
- Web Presentation: A static webpage hosted via GitHub Pages, showcasing the visualized data in an accessible and interactive format, complete with the ability to view graphs for different cities.


## Running the Project
This project consists of multiple scripts that handle different stages of the data pipeline. Below are the instructions on how to run each part of the project:

### Setting Up the Environment
Before running the scripts, make sure to set up your Python environment and install all required dependencies:

```
# Create a virtual environment (optional but recommended)
python -m venv venv
# Activate the virtual environment
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the required packages
pip install -r requirements.txt
```

### Fetching Weather Data
To fetch historical weather data for the year 2023:

```
python -m src.fetch_weather
```
This will collect data from the OpenWeatherMap API and store it in the database.


### Processing Weather Data
Once the data is fetched, process it to a structured format:

```
python -m src.process_data
```
This script will transform the raw data into processed data, ready for analysis.

### Analyzing Weather Data
To generate visualizations from the processed data:

```
python -m src.analyze_data
```
Running this script will create graphs representing the weather trends and save them to the graphs directory.

### Viewing the Visualizations
After running the analysis, the generated graphs can be viewed in the graphs directory or through the static webpage if you are using GitHub Pages to host the visualizations.

## Configuration

Before running the project, you must provide your OpenWeatherMap API key. This can be done by setting an environment variable named `OPENWEATHERMAP_API_KEY`.

Alternatively, you can use a `.env` file placed in the root of the project with the following content:
