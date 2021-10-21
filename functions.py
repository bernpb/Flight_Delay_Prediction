import pandas as pd
# Metrics
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix

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


def dummify(df, column):
    
    temp_list = list(df[column])
    temp_df = pd.DataFrame(temp_list, columns = [column])
    dummy_df = pd.get_dummies(temp_df, columns = [column], prefix = ['type_is'])
    return dummy_df


def binary_classifier_metrics(y_test, y_pred):
    
    """
    Quick function to return metrics for binary classification models.
    
    Requires the imports of the functions below.
    """
    
    print('Accuracy: ', accuracy_score(y_test, y_pred))
    print('F1 score: ', f1_score(y_test, y_pred))
    print('Precision score: ', precision_score(y_test, y_pred))
    print('Recall score: ', recall_score(y_test, y_pred))
    print('Confusion Matrix: \n', confusion_matrix(y_test, y_pred))

    
def multiclassifier_metrics(y_test, y_pred):
    
    """
    Quick function to return metrics for multi-classification models.
    
    Requires the imports of the functions below.
    """
    
    print('Accuracy: ', accuracy_score(y_test, y_pred))
    print('F1 score: ', f1_score(y_test, y_pred,
                                average = 'micro'))
    print('Precision score: ', precision_score(y_test, y_pred,
                                              average = 'micro'))
    print('Recall score: ', recall_score(y_test, y_pred,
                                        average = 'micro'))
    print('Confusion Matrix: \n', confusion_matrix(y_test, y_pred))
    

def regression_metrics(y_test, y_pred):
    print('R2 Score: ', r2_score(y_test, y_pred))
    print('Mean Absolute Error: ', mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error: ', mean_squared_error(y_test, y_pred))
    
    
def grid_search_results(grid_search, X, y):
    """
    Returns grid search results in a readable format
    """
    
    print('Best Score: ',grid_search.score(X, y, ))
    print('Best Params: ', grid_search.best_params_)

def grid_search_results(grid_search, X, y):
    print('Best Score: ',grid_search.score(X, y, ))
    print('Best Params: ', grid_search.best_params_)
    
