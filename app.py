import streamlit as st
import requests

# Page Config
st.set_page_config(
    page_title="Weather App",
    page_icon="⛅",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main-header {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #333;
        text-align: center;
    }
    .weather-card {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-top: 2rem;
    }
    .metric-value {
        font-size: 3rem;
        font-weight: bold;
        color: #007bff;
    }
    .metric-label {
        font-size: 1.2rem;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# API Key
API_KEY = "c1c48b686498401582a214207241008"

def get_weather(city_name):
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}&aqi=yes"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return None

# UI Layout
st.markdown("<h1 class='main-header'>⛅ Weather App</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    city_input = st.text_input("", placeholder="Enter City Name (e.g., New York)")
    search_btn = st.button("Get Weather", use_container_width=True)

if search_btn and city_input:
    with st.spinner("Fetching weather data..."):
        data = get_weather(city_input)
    
    if data:
        location = data['location']
        current = data['current']
        
        st.markdown(f"""
        <div class="weather-card">
            <h2>{location['name']}, {location['country']}</h2>
            <p style="color: #666;">{location['localtime']}</p>
            <div style="margin: 20px 0;">
                <img src="http:{current['condition']['icon']}" width="100" />
                <div class="metric-value">{current['temp_c']}°C</div>
                <div class="metric-label">{current['condition']['text']}</div>
            </div>
            <div style="display: flex; justify-content: space-around; margin-top: 20px;">
                <div>
                    <strong>Humidity</strong><br/>
                    {current['humidity']}%
                </div>
                <div>
                    <strong>Wind</strong><br/>
                    {current['wind_kph']} kph
                </div>
                <div>
                    <strong>Feels Like</strong><br/>
                    {current['feelslike_c']}°C
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.error("City not found or API error. Please try again.")

elif search_btn and not city_input:
    st.warning("Please enter a city name.")
