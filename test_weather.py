import unittest
from main import get_weather, format_output


class TestWeatherApp(unittest.TestCase):
        
    def test_format_output_valid_data(self):
        # Test with valid weather data
        weather_data = {
            'location': 'London, GB',
            'description': 'Clear',
            'temperature': 15.0,
            'humidity': 77,
            'wind_speed': 3.09,
            'sunrise_time': '06:08:38',
            'sunset_time': '17:48:17'
        }
        expected_output = "Location: London, GB\n" \
                          "Conditions: Clear\n" \
                          "Temperature: 15.00°C\n" \
                          "Humidity: 77%\n" \
                          "Wind Speed: 3.09 m/s\n" \
                          "Sunrise: 06:08:38\n" \
                          "Sunset: 17:48:17"
        output = format_output(weather_data)
        self.assertEqual(output, expected_output)

    def test_format_output_invalid_data(self):
        # Test with invalid weather data (i.e. error message)
        weather_data = {'error': 'Invalid city name'}
        expected_output = "Error: Invalid city name"
        output = format_output(weather_data)
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
