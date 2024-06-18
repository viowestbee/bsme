country_data = {
    'India': '6:00 AM',
    'Afghanistan': '10:30 AM',
    'Iran': '9:30 AM',
    'Turkmenistan': '3:00 AM',
    # Add more country-time pairs here
    # ...
}

# Function to check if the given time is correct
def check_time(country, time):
    if country in country_data:
        if country_data[country] == time:
            return True
        else:
            return False
    else:
        return False

# Example usage
country = 'India'
time = '6:00 AM'

if check_time(country, time):
    print(f"The time for {country} is correct.")
else:
    print(f"The time for {country} is incorrect.")