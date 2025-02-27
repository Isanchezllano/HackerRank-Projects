import calendar


def find_day(date_str):
    month, day, year = map(int, date_str.split())  # Convert input to integers
    day_of_week = calendar.weekday(year, month, day)  # Get the weekday index (0 = Monday, 6 = Sunday)
    return calendar.day_name[day_of_week].upper()  # Return the day name in uppercase



