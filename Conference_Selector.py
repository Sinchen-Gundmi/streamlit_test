import streamlit as st
import numpy as np
import hashlib
import time

def temperature_to_city(temperature):
    cities = ["Houston", "Chicago", "Atlanta", "New Jersey", "Dallas"]
    if temperature < 50 or temperature > 75:
        return None, "Temperature out of range. Please enter a temperature between 50 and 75."

    # Simple hash function to distribute temperatures evenly across cities
    hash_val = int(hashlib.sha256(str(temperature).encode()).hexdigest(), 16)
    index = hash_val % len(cities)
    return cities[index], ""

# Streamlit UI
def run_app():
    st.title("🌍 Workshop Venue Selector")
    
    # Use columns to center the input form
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        temperature = st.number_input("Temperature (°F)", min_value=50, max_value=75, value=62, step=1)

    if st.button("Select Venue"):
        with st.spinner('Calculating...'):
            # Countdown
            placeholder = st.empty()
            for i in range(3, 0, -1):
                placeholder.markdown(f"<h1 style='text-align: center;'>{i}</h1>", unsafe_allow_html=True)
                time.sleep(1)
            placeholder.empty()

            # Display result
            city, error = temperature_to_city(temperature)
            if city:
                st.markdown(f"<h1 style='text-align: center; color: green;'>{city}</h1>", unsafe_allow_html=True)
            else:
                st.error(error)
    else:
        # Instruction
        st.write("Enter the current temperature and click 'Select Venue' to find out where the next workshop will be held!")

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
