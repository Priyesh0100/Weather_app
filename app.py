import streamlit as st
import requests



def get_weather_data(city):
    api_key = "319143c554605e34e24f54c8cbbc9d87"  # Replace with your API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for error status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching weather data: {e}")
        return None

def main():
    st.title("Weather App")

    city = st.text_input("Enter a city:")

    if st.button("Get Weather"):
        weather_data = get_weather_data(city)

        if weather_data:
            temperature = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]

            st.success(f"Weather in {city}:")
            st.write(f"Temperature: {temperature:.2f} °C")
            st.write(f"Description: {description}")
            st.write(f"Humidity: {humidity}%")
            st.write(f"Wind Speed: {wind_speed} m/s")



if __name__ == "__main__":
    main()