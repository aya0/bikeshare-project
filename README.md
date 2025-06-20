<<<<<<< HEAD
# Bikeshare Data Analysis

This project allows you to explore US bikeshare data for three major cities: Chicago, New York City, and Washington. The script provides statistics and insights based on user-specified filters such as city, month, and day of the week.

## Features
- Interactive command-line interface for selecting city, month, and day
- Calculates and displays:
  - Most frequent times of travel
  - Most popular stations and trips
  - Trip duration statistics
  - User statistics (user types, gender, birth year)
- Option to view raw data in increments of 5 rows

## How to Use
1. Ensure you have Python 3 and `pandas` installed.
2. Place the city data CSV files (`chicago.csv`, `new_york_city.csv`, `washington.csv`) in the same directory as `bikeshare.py`.
3. Run the script:
   ```bash
   python bikeshare.py
   ```
4. Follow the prompts to select a city, month, and day, and view the statistics.

## Requirements
- Python 3.x
- pandas

## File Structure
- `bikeshare.py`: Main script for data analysis
- `README.md`: This file
- `chicago.csv`, `new_york_city.csv`, `washington.csv`: Data files (not included)

## Notes
- Gender and birth year data are not available for all cities.
- The script is designed for educational purposes as part of a Udacity project. 
