# import folium as folium
#
# data = [{"lat": 28.7041, "lon": 77.1025, "name": "Delhi"}]
# map = folium.Map(location=[28.7041, 77.1025], zoom_start=5)
# for loc in data:
#     folium.Marker([loc['lat'], loc['lon']], popup=loc['name']).add_to(map)
# map.save("map.html")

# import folium
# import json
#
# # Simulated JSON data (pretend it's from an API)
# mock_json = '''
# [
#   {"city": "Delhi", "lat": 28.6139, "lon": 77.2090},
#   {"city": "Mumbai", "lat": 19.0760, "lon": 72.8777},
#   {"city": "Bangalore", "lat": 12.9716, "lon": 77.5946},
#   {"city": "Kolkata", "lat": 22.5726, "lon": 88.3639},
#   {"city": "Chennai", "lat": 13.0827, "lon": 80.2707}
# ]
# '''
#
# # Step 1: Parse JSON normally
# locations = json.loads(mock_json)
#
# # Step 2: Create folium map
# m = folium.Map(location=[22, 80], zoom_start=5)
#
# # Step 3: Add each city as a marker
# for city in locations:
#     folium.Marker(
#         location=[city["lat"], city["lon"]],
#         popup=city["city"],
#         icon=folium.Icon(color="green", icon="info-sign")
#     ).add_to(m)
#
# # Step 4: Save the map
# m.save("indian_cities_map.html")
# print("✅ Indian cities map saved as 'indian_cities_map.html'")

import requests
import folium

# # Step 1: Fetch earthquake data
# url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
# response = requests.get(url)
# data = response.json()
#
# # Step 2: Create map (default tile: OpenStreetMap)
# m = folium.Map(location=[20, 0], zoom_start=2)
#
# # Step 3: Add earthquake markers
# for feature in data["features"]:
#     coords = feature["geometry"]["coordinates"]
#     lon, lat = coords[0], coords[1]
#     mag = feature["properties"]["mag"]
#     place = feature["properties"]["place"]
#
#     if mag is None:
#         continue
#
#     folium.CircleMarker(
#         location=[lat, lon],
#         radius=mag * 2,
#         color="red",
#         fill=True,
#         fill_opacity=0.6,
#         popup=f"{place}<br>Magnitude: {mag}"
#     ).add_to(m)
#
# # Step 4: Save to file
# m.save("earthquake_map.html")
# print("✅ Map saved as 'earthquake_map.html'")

import requests
import folium

# 👉 Source: https://api.waqi.info (World Air Quality Index)
# 📌 You’ll need a free API key from: https://aqicn.org/data-platform/token/#/

API_KEY = "e8869f17eaa56650330f20533d5e1290c000sasa"  # Replace with your real API key
cities = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Lucknow"]

def get_aqi(city):
    url = f"https://api.waqi.info/feed/{city}/?token={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "ok":
        return data["data"]["aqi"], data["data"]["city"]["geo"]
    return None, None

# Initialize map
m = folium.Map(location=[22, 80], zoom_start=5)

# Add markers
for city in cities:
    aqi, coords = get_aqi(city)
    if aqi and coords:
        folium.CircleMarker(
            location=coords,
            radius=8,
            color="green" if aqi < 100 else "orange" if aqi < 200 else "red",
            fill=True,
            fill_opacity=0.7,
            popup=f"{city}<br>AQI: {aqi}"
        ).add_to(m)

m.save("india_aqi_map.html")
print("✅ AQI map saved as 'india_aqi_map.html'")