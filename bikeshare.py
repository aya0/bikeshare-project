import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}

def get_filters():
    print("Hello! Let's explore some US bikeshare data!")
    city = ""
    while city not in CITY_DATA:
        city = input("Enter city (Chicago, New York City, Washington): ").lower().strip()
        if city not in CITY_DATA:
            print("Please enter Chicago, New York City, or Washington.")
        if not city:
            print("City cannot be empty.")
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = ""
    while month not in months:
        month = input("Enter month (all, January, February, ..., June): ").lower().strip()
        if month not in months:
            print("Please enter all or a month from January to June.")
        if not month:
            print("Month cannot be empty.")
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ""
    while day not in days:
        day = input("Enter day of week (all, Monday, Tuesday, ..., Sunday): ").lower().strip()
        if day not in days:
            print("Please enter all or a day of the week.")
        if not day:
            print("Day cannot be empty.")
    print("-" * 40)
    return city, month, day

def load_data(city, month, day):

    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_number = months.index(month) + 1
        df = df[df['month'] == month_number]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    month_number = df['month'].mode()[0]
    most_common_month = months[month_number - 1]
    print(f"Most common month: {most_common_month}")
    most_common_day = df['day_of_week'].mode()[0]
    print(f"Most common day of week: {most_common_day}")
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print(f"Most common start hour: {most_common_hour}")
    print(f"\nThis took {time.time() - start_time} seconds.")
    print("-" * 40)

def station_stats(df):

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()
    most_common_start = df['Start Station'].mode()[0]
    print(f"Most common start station: {most_common_start}")
    most_common_end = df['End Station'].mode()[0]
    print(f"Most common end station: {most_common_end}")
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    most_common_trip = df['trip'].mode()[0]
    print(f"Most common trip: {most_common_trip}")
    print(f"\nThis took {time.time() - start_time} seconds.")
    print("-" * 40)

def trip_duration_stats(df):

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time} seconds")
    print(f"\nThis took {time.time() - start_time} seconds.")
    print("-" * 40)

def user_stats(df):

    print("\nCalculating User Stats...\n")
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
    print(f"\nThis took {time.time() - start_time} seconds.")
    print("-" * 40)

def display_raw_data(df):

    if df.empty:
        print("No data available to display.")
        return
    row_index = 0
    while True:
        show_data = input("\nWould you like to see 5 rows of raw data? Enter yes or no: ").lower().strip()
        if show_data == 'yes':
            if row_index >= len(df):
                print("No more data to display.")
                break
            print(df.iloc[row_index:row_index + 5])
            row_index = row_index + 5
        elif show_data == 'no':
            break
        else:
            print("Please enter yes or no.")

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df is None or df.empty:
            print("No data available. Please try again.")
            continue
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input("\nWould you like to restart? Enter yes or no: ").lower().strip()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
