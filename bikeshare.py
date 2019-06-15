import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = []
    #print(type(city_list))
    for city, filename in CITY_DATA.items():
        print(city)
        city_list.append(city)
        
    print("Please type city name that you want to investigate. Choose one from the followings.")
    print(city_list)
    city = input()
    #until get correct choice, let's loop here
    while city not in city_list:
        print("Your type isn't acceptable. Please type city name that you want to investigate. Choose one from the followings.")
        print(city_list)
        city = input()
   
    month_list = ["january", "feburary", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "all"]
    # TO DO: get user input for month (all, january, february, ... , june)
    print("Please type month that you would like to filter. Enter 'all' if you don't want to filter by month")
    print(month_list)
    month = input()
    #until get correct choice, let's loop here
    while month not in month_list:
        print("Your type isn't acceptable. Please retry.")
        print(month_list)
        month = input()
  
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturaday", "sunday", "all"]
    print("Please type day that you would like to filter. Enter 'all' if you don't want to filter by day")
    print(day_list)
    day = input()
    #utilt get correct choice, let's loop here.
    while day not in day_list:
        print("Your type isn't acceptable. Please retry.")
        print(day_list)
        day = input()
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.weekday_name
    if month != "all":
        months = ["january", "feburary", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
        month = months.index(month) + 1
        df = df[df["month"] == month ]
    if day !=  "all":
        df = df[df["day"] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    print("the most common month")
    print(df["month"].mode()[0])

    # TO DO: display the most common day of week
    print("the most common day of week")
    print(df["day"].mode()[0])

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    print("the most common start hour")
    print(df["hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("display most commonly used start station")
    print(df["Start Station"].mode()[0])

    # TO DO: display most commonly used end station
    print("display most commonly used end station")
    print(df["End Station"].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("display total travel time")
    print("{} hours".format(df["Trip Duration"].sum(skipna=True)/60))
    # TO DO: display mean travel time
    print("display mean travel time")
    print("{} min".format(df["Trip Duration"].mean(skipna=True)/60))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Display counts of user types")
    print(df["User Type"].value_counts(dropna=True))

    # TO DO: Display counts of gender
    if ("Gender") in df.index:
        print("Display counts of gender")
        print(df["Gender"].value_counts(dropna=True))
    else:
          print("No Gender Column in the DB")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    print("Display earliest, most recent, and most common year of birth")
    if "Birth Year" in df.index:
        print("earliest year of birth")
        print(df["Birth Year"].min())
        print("most recent year of birth")
        print(df["Birth Year"].max())
        print("most common year of birth")
        print(df["Birth Year"].mode()[0])
    else:
        print("There is no Brith Year info regarding your choosing city DB.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
