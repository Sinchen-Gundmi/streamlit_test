import streamlit as st
import numpy as np
import hashlib

def temperature_to_city(temperature):
    cities = ["Houston", "Chicago", "Atlanta", "New Jersey", "Dallas"]
    if temperature < 50 or temperature > 75:
        return "Temperature out of range. Please enter a temperature between 50 and 75."

    # Simple hash function to distribute temperatures evenly across cities
    hash_val = int(hashlib.sha256(str(temperature).encode()).hexdigest(), 16)
    index = hash_val % len(cities)
    return cities[index]

# Streamlit UI
def run_app():
    st.title("Workshop Venue Selector")
    st.write("Enter the current temperature to select the venue for the next meeting.")

    temperature = st.number_input("Temperature (°F)", min_value=50, max_value=75, value=50, step=1)
    if st.button("Select Venue"):
        city = temperature_to_city(temperature)
        st.success(f"The next workshop will be in {city}!")

    # Enhancements: Add some CSS for styling
    st.markdown(
        """
        <style>
        .stButton>button {
            width: 100%;
            border-radius: 20px;
            border: 2px solid #4CAF50;
            color: white;
            background-color: #4CAF50;
            padding: 14px 20px;
            margin: 8px 0;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_app()
