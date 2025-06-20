import time
import pandas as pd

# Constants
CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
MONTHS_TO_NAME = {i + 1: month.capitalize() for i, month in enumerate(MONTHS)}

def get_valid_input(prompt, valid_options, empty_message="Input cannot be empty."):
    """Prompt user for input and validate against valid options."""
    while True:
        user_input = input(prompt).lower().strip()
        if not user_input:
            print(empty_message)
            continue
        if user_input in valid_options:
            return user_input
        print(f"Please enter one of: {', '.join(valid_options)}.")

def print_section_header(title):
    """Print a standardized section header."""
    print(f"\n=== {title} ===\n")

def get_filters():
    """Get user input for city, month, and day filters."""
    print("Hello! Let's explore some US bikeshare data!")
    cities = list(CITY_DATA.keys())
    city = get_valid_input("Enter city (Chicago, New York City, Washington): ", cities)
    valid_months = ['all'] + MONTHS
    month = get_valid_input("Enter month (all, January, February, ..., June): ", valid_months)
    valid_days = ['all'] + DAYS
    day = get_valid_input("Enter day of week (all, Monday, Tuesday, ..., Sunday): ", valid_days)
    print("-" * 40)
    return city, month, day

def load_data(city, month, day):
    """Load and filter bikeshare data based on city, month, and day."""
    try:
        df = pd.read_csv(CITY_DATA[city])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        if month != 'all' or day != 'all':
            df['month'] = df['Start Time'].dt.month
            df['day_of_week'] = df['Start Time'].dt.day_name()
            if month != 'all':
                month_number = MONTHS.index(month) + 1
                df = df[df['month'] == month_number]
            if day != 'all':
                df = df[df['day_of_week'] == day.title()]
        return df
    except FileNotFoundError:
        print(f"Error: Data file for {city} not found.")
    except Exception as e:
        print(f"Error loading data for {city}: {str(e)}")
    return None

def time_stats(df):
    """Display statistics on the most frequent times of travel."""
    print_section_header("Most Frequent Times of Travel")
    start_time = time.time()
    most_common_month = MONTHS_TO_NAME[df['month'].mode()[0]]
    print(f"Most common month: {most_common_month}")
    most_common_day = df['day_of_week'].mode()[0]
    print(f"Most common day: {most_common_day}")
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    print(f"Most common start hour: {most_common_hour}")
    print(f"Calculation took {time.time() - start_time:.3f} seconds.")
    print("-" * 40)

def station_stats(df):
    """Display statistics on the most popular stations and trip."""
    print_section_header("Popular Stations and Trip")
    start_time = time.time()
    most_common_start = df['Start Station'].mode()[0]
    print(f"Most common start station: {most_common_start}")
    most_common_end = df['End Station'].mode()[0]
    print(f"Most common end station: {most_common_end}")
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"Most common trip: {most_common_trip[0]} to {most_common_trip[1]}")
    print(f"Calculation took {time.time() - start_time:.3f} seconds.")
    print("-" * 40)

def trip_duration_stats(df):
    """Display statistics on trip duration."""
    print_section_header("Trip Duration")
    start_time = time.time()
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time:.2f} seconds")
    print(f"Calculation took {time.time() - start_time:.3f} seconds.")
    print("-" * 40)

def user_stats(df):
    """Display statistics on user types, gender, and birth year."""
    print_section_header("User Statistics")
    start_time = time.time()
    user_types = df['User Type'].value_counts()
    print("User Type Counts:")
    print(user_types)
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nGender Counts:")
        print(gender_counts)
    else:
        print("\nGender data not available for this city.")
    if 'Birth Year' in df.columns:
        earliest_birth = int(df['Birth Year'].min())
        most_recent_birth = int(df['Birth Year'].max())
        most_common_birth = int(df['Birth Year'].mode()[0])
        print(f"\nEarliest birth year: {earliest_birth}")
        print(f"Most recent birth year: {most_recent_birth}")
        print(f"Most common birth year: {most_common_birth}")
    else:
        print("\nBirth year data not available for this city.")
    print(f"Calculation took {time.time() - start_time:.3f} seconds.")
    print("-" * 40)

def display_raw_data(df):
    """Display raw data in pages of 5 rows with forward/backward navigation."""
    if df.empty:
        print("No data available to display.")
        return
    row_index = 0
    page_size = 5
    while True:
        prompt = "\nShow raw data? Enter 'next' (next 5 rows), 'prev' (previous 5 rows), or 'no' (exit): "
        action = get_valid_input(prompt, ['next', 'prev', 'no'], "Please enter 'next', 'prev', or 'no'.")
        if action == 'no':
            break
        elif action == 'next':
            if row_index >= len(df):
                print("No more data to display.")
                continue
            print(df.iloc[row_index:row_index + page_size])
            row_index += page_size
        elif action == 'prev':
            row_index = max(0, row_index - page_size)
            print(df.iloc[row_index:row_index + page_size])

def main():
    """Main function to run the bikeshare data analysis."""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df is None:
            continue
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        if get_valid_input("\nWould you like to restart? Enter yes or no: ", ['yes', 'no']) != 'yes':
            break

if __name__ == "__main__":
    main()