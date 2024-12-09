import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium
import folium

def main():
    st.title("Interactive Map: Select Your Location")
    st.write("Use the map below to select your location or search for it using the input box.")

    # Create a geolocator
    geolocator = Nominatim(user_agent="streamlit_location_selector")

    # Add input for location search
    search_location = st.text_input("Search for a location", "")

    if search_location:
        with st.spinner("Searching for location..."):
            try:
                location = geolocator.geocode(search_location)
                if location:
                    st.success(f"Location found: {location.address}")
                    selected_location = [location.latitude, location.longitude]
                else:
                    st.error("Location not found. Try a different search.")
                    selected_location = [0, 0]  # Default to the world map center
            except Exception as e:
                st.error(f"An error occurred: {e}")
                selected_location = [0, 0]
    else:
        selected_location = [0, 0]  # Default to the world map center

    # Create map with Folium
    m = folium.Map(location=selected_location, zoom_start=10)
    folium.Marker(selected_location, popup="Selected Location").add_to(m)

    # Display map
    st_data = st_folium(m, width=700, height=500)

    if st_data["last_clicked"]:
        lat, lon = st_data["last_clicked"]["lat"], st_data["last_clicked"]["lng"]
        st.write(f"Selected Coordinates: Latitude: {lat}, Longitude: {lon}")
    else:
        st.write("Click on the map to select a location.")

if __name__ == "__main__":
    main()
