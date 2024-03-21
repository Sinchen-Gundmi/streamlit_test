import streamlit as st
import numpy as np
import hashlib
import time
import pandas as pd

# City coordinates for mapping, including latitude, longitude, and a suitable zoom level for each city
city_locations = {
    "Denver": {"coords": (39.7392, -104.9903), "zoom": 10},
    "Dallas": {"coords": (32.7767, -96.7970), "zoom": 10},
    "McLean": {"coords": (38.9339, -77.1773), "zoom": 11},
    "Hoboken": {"coords": (40.7433, -74.0288), "zoom": 13},
    "Chicago": {"coords": (41.8781, -87.6298), "zoom": 10},
    "Houston": {"coords": (29.7604, -95.3698), "zoom": 10},
    "Atlanta": {"coords": (33.7490, -84.3880), "zoom": 10}
}

def temperature_to_city(temperature):
    cities = list(city_locations.keys())
    if temperature < 25 or temperature > 70:
        return None, "Temperature out of range. Please enter a temperature between 25 and 70."

    # Adjusting hash function for a wider range and ensuring distribution
    hash_val = int(hashlib.sha256(str(temperature).encode()).hexdigest(), 16)
    index = hash_val % len(cities)
    return cities[index], ""

def plot_city_on_map(city):
    if city in city_locations:
        location = city_locations[city]["coords"]
        zoom_level = city_locations[city]["zoom"]
        map_data = pd.DataFrame([location], columns=['lat', 'lon'])
        st.map(map_data, zoom=zoom_level)
    else:
        st.error("City location not found.")

# Streamlit UI
def run_app():
    st.title("🌍 All Hands Venue Selector")

    # Input for temperature
    temperature = st.slider("Current Temperature (°F) of Boston\nBlahblahblah", min_value=25, max_value=70, value=25, step=1)

    if st.button("Select Venue"):
        with st.spinner('Calculating...'):
            # Countdown
            placeholder = st.empty()
            for i in range(3, 0, -1):
                placeholder.markdown(f"<h1 style='text-align: center;'>{i}</h1>", unsafe_allow_html=True)
                time.sleep(1)
            placeholder.empty()

            # Determine city and display result
            city, error = temperature_to_city(temperature)
            if city:
                st.markdown(f"<h1 style='text-align: center; color: green;'>{city}</h1>", unsafe_allow_html=True)
                plot_city_on_map(city)
            else:
                st.error(error)
    else:
        # Instruction
        st.write("Adjust the temperature and click 'Select Venue' to find out where the next All Hands will be held!")

    # CSS for styling
    st.markdown(
        """
        <style>
        .stButton>button {
            width: 100%;
            border: 2px solid #4CAF50;
            border-radius: 25px;
            font-size: 20px;
            font-weight: bold;
            color: white;
            background-color: #4CAF50;
            padding: 10px 24px;
            margin: 10px 0;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_app()
