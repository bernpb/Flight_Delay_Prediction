def statebreaker(city_state):
    """
    Params:  
    city_state - A string consisting of a city name and a state abbreviation
    
    Function:  
    Splits the string, extracting the state abbreviation.
    """
    split_list = city_state.split(',')
    return split_list[-1]


def delay_binarizer(input_col):
    
    """
    Params:
    input_col - an input of time in minutes
    
    Function:
    Returns 0 if the time is positive (delayed) or 1 if the flight is early/on time"""
    if input_col > 0:
        return 0
    else:
        return 1

    
def get_hour(time):
    
    """
    Params - A time in format HHMM.0
    
    Returns  the two digits representing the hour of the flight
    """
    
    s = str(int(time))
    if len(s) <= 2:
        return 0
    else:
        return int(s[:-2])
    

def get_min(time):
    
    """
    Params - A time in format HHMM.0
    
    Returns  the two digits representing the minutes of the flight
    """
    s = str(int(time))
    if len(s) <=2:
        return(int(s))
    else:
        return (int(s[-2:]))

def haul_type(elapsed_time):
    
    """
    Params - Duration of a flight
    
    Returns -  A haul type as defined below:
    
        Short - Less than 180 minutes
        Medium - Between 180 and 360 minutes
        Long - Over 360 minutes
     """
    if elapsed_time < 180:
        return 'Short'
    elif 180 < elapsed_time < 360:
        return 'Medium'
    else:
        return 'Long'
    
# Function to assign a time of day label to the dataframes.  
# Allows for better matching of weather to our flights dataframe
def time_of_day(hour):
    """
    Input an hour of the day.  
    Output Morning, Afternoon, Evening, Night
    """
    if 0 <= hour < 6:
        return 'Night'
    elif 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return'Afternoon'
    elif 18 <= hour:
        return 'Evening'
    