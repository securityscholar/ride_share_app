import streamlit as st
import folium
from streamlit_folium import st_folium

def main():
    st.title("Interactive Map: Select Your Location")
    st.write("Click on the map to select your location.")

    # Default location (center of the world)
    default_location = [0, 0]
    selected_location = st.session_state.get("selected_location", default_location)

    # Initialize the map
    m = folium.Map(location=selected_location, zoom_start=2)

    # Add a marker for the previously selected location
    if "selected_location" in st.session_state:
        folium.Marker(
            st.session_state["selected_location"],
            popup="Your Selected Location",
            icon=folium.Icon(color="blue")
        ).add_to(m)

    # Add a click listener to the map
    m.add_child(folium.ClickForMarker(popup="Selected Location"))

    # Display the map
    map_data = st_folium(m, width=700, height=500)

    # Capture the coordinates of the last clicked location
    if map_data and map_data.get("last_clicked"):
        lat = map_data["last_clicked"]["lat"]
        lon = map_data["last_clicked"]["lng"]
        st.session_state["selected_location"] = [lat, lon]
        st.write(f"Selected Coordinates: Latitude: {lat}, Longitude: {lon}")

if __name__ == "__main__":
    main()
