# Weather Report

This Python script provides the current temperature of a specified city using the WeatherAPI. It also uses the `win32com` library to convert the text into speech.

## Usage

1. Install the necessary libraries:

```bash
pip install requests
```

2. Make sure you have the `win32com` library installed. If not, install it using:

```bash
pip install pywin32
```

3. Run the script:

```bash
python weather_report.py
```

4. Enter the city for which you want to get the weather report.

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

[Aniruddh R Panicker](https://github.com/RPAniruddh)

---
