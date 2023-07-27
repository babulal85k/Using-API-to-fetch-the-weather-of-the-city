import requests

def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def get_temperature(api_key, city_name):
    try:
        # Construct the API URL with the city name and API key
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        
        # Send a GET request to the API
        response = requests.get(api_url)
        
        # Check the response status code
        if response.status_code == 200:
            # Parse the response data (assuming it is in JSON format)
            data = response.json()
            
            # Extract the temperature from the data
            temperature_kelvin = data["main"]["temp"]
            
            # Convert the temperature from Kelvin to Celsius
            temperature_celsius = kelvin_to_celsius(temperature_kelvin)
            
            print(f"The temperature in {city_name} is {temperature_celsius:.2f}°C.")
            
        else:
            print(f"Error: Failed to fetch data for {city_name}.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        

# Example usage:
if __name__ == "__main__":
    api_key = "9ebdbfcb3cdd54486ca7d520101f6290"  # Replace with your actual API key
    city_name = input("Enter the city name: ")
    get_temperature(api_key, city_name)
