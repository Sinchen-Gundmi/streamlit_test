import streamlit as st
import numpy as np
import hashlib
import time
import pandas as pd

def temperature_to_city(temperature):
    cities = {
        "Houston": (29.7604, -95.3698),
        "Chicago": (41.8781, -87.6298),
        "Atlanta": (33.7490, -84.3880),
        "New Jersey": (40.7357, -74.1724),  # Using Newark for New Jersey
        "Dallas": (32.7767, -96.7970)
    }
    if temperature < 50 or temperature > 75:
        return None, "Temperature out of range. Please enter a temperature between 50 and 75.", None

    # Simple hash function to distribute temperatures evenly across cities
    hash_val = int(hashlib.sha256(str(temperature).encode()).hexdigest(), 16)
    city_names = list(cities.keys())
    index = hash_val % len(city_names)
    city_name = city_names[index]
    return city_name, "", cities[city_name]

# Streamlit UI
def run_app():
    st.title("🌍 Workshop Venue Selector")
    
    # Use columns to center the input form
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        temperature = st.number_input("Temperature in Boston (°F)", min_value=50, max_value=75, value=62, step=1)

    if st.button("Select Venue"):
        with st.spinner('Calculating...'):
            # Countdown
            placeholder = st.empty()
            for i in range(3, 0, -1):
                placeholder.markdown(f"<h1 style='text-align: center;'>{i}</h1>", unsafe_allow_html=True)
                time.sleep(1)
            placeholder.empty()

            # Display result and map
            city_name, error, coords = temperature_to_city(temperature)
            if city_name:
                st.markdown(f"<h1 style='text-align: center; color: green;'>{city_name}</h1>", unsafe_allow_html=True)
                # Display the map
                df = pd.DataFrame([coords], columns=['lat', 'lon'])
                st.map(df)
            else:
                st.error(error)
    else:
        # Instruction
        st.write("Enter the current temperature and click 'Select Venue' to find out where the next All Hands will be held!")

    # Enhancements: Add some CSS for styling globally
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
