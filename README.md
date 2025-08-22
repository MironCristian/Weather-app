Weather App

A simple desktop application built in Python that displays the current weather and a relevant weather icon for a user-entered city.

Features

Graphical User Interface (GUI) built with Tkinter

Search for any city in the world

Display of the current temperature and a textual weather description

Dynamic weather icons fetched in real time

Technologies Used

Python

Tkinter for the GUI

Requests for API calls

Pillow (PIL) for processing and displaying images

Public APIs:

Open-Meteo Geocoding for converting city names into coordinates

Open-Meteo Weather for weather data

OpenWeatherMap Icons for visual icons

How to Run

Clone this repository:

git clone https://github.com/MironCristian/weather-app.git
cd weather-app


Create and activate a virtual environment:

python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate


Install the dependencies:

pip install -r requirements.txt


Run the application:

python main.py