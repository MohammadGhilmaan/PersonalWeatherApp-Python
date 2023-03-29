import unittest
from main import get_weather, format_output


class TestWeatherApp(unittest.TestCase):
    def test_get_weather_valid_city(self):
        # Test with a valid city name
        city = "London"
        weather_data = get_weather(city)
        self.assertIsInstance(weather_data, dict)
        self.assertNotIn('error', weather_data)
        self.assertIn('location', weather_data)
        self.assertIn('description', weather_data)
        self.assertIn('temperature', weather_data)
        self.assertIn('humidity', weather_data)
        self.assertIn('wind_speed', weather_data)
        self.assertIn('sunrise_time', weather_data)
        self.assertIn('sunset_time', weather_data)

    def test_get_weather_invalid_city(self):
        # Test with an invalid city name
        city = "Invalid City"
        weather_data = get_weather(city)
        self.assertIsInstance(weather_data, dict)
        self.assertIn('error', weather_data)

    def test_format_output_invalid_data(self):
        # Test with invalid weather data (i.e. error message)
        weather_data = {'error': 'Invalid city name'}
        expected_output = "Error: Invalid city name"
        output = format_output(weather_data)
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
