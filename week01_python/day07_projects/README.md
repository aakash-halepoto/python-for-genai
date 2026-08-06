# Weather CLI

A command-line tool that fetches live current weather for any location using the Open-Meteo API.

## What it does
- Takes a city name and coordinates
- Fetches real-time temperature and wind speed
- Handles failed requests gracefully

## Tech used
- Python
- requests (HTTP calls)
- Open-Meteo API (free, no key required)

## How to run
\`\`\`bash
pip install requests
python weather.py
\`\`\`

## Example output
\`\`\`
Hyderabad: 31.2°C, wind 12.5 km/h
Karachi: 29.8°C, wind 18.3 km/h
\`\`\`

## What I learned
Building this reinforced working with REST APIs, parsing nested JSON responses, and handling request failures gracefully.