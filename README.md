# Weather Report with Text-to-Speech

This Python script retrieves and announces the current temperature of a specified city using the WeatherAPI. It utilizes the `requests` library to make API requests and the `win32com` library for text-to-speech functionality.

## Usage

1. Get an API key by signing up at [WeatherAPI](https://www.weatherapi.com/signup.aspx).

2. Replace `'API_KEY'` in the `url` variable with your actual API key.

3. Install the necessary libraries:

```bash
pip install requests
```

4. Make sure you have the `win32com` library installed. If not, install it using:

```bash
pip install pywin32
```

5. Run the script:

```bash
python weather_report.py
```

6. Enter the city for which you want to get the weather report.

The script will retrieve and display the current temperature along with a spoken message.

## Example

```plaintext
Enter the city: New York

The Temperature of New York is 20°C
```

## Note

- Make sure you have Python installed on your system.
- The script uses the WeatherAPI, so an internet connection is required.
- Ensure that you have the `win32com` library installed for text-to-speech functionality.

## Author

[Aniruddh](https://github.com/RPAniruddh)

---
