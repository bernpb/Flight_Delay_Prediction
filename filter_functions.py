import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.feature_selection import VarianceThreshold

def drop_low_var(x, df):
    
    ''' 
    Takes in a DataFrame and a variance, x (float between 0 and 1) as parameters.
    Drops any columns with a lower varaince than X.
    '''   
    
    # Set variance threshold and apply its fit transform to the dataframe
    vt = VarianceThreshold(x)
    df_transformed = vt.fit_transform(df)
    
    # use get_support() to restore the missing column names
    selected_cols = df.columns[vt.get_support()]
    df_transformed = pd.DataFrame(df_transformed, columns = selected_cols)
    
    return df_transformed



def drop_x_missing(x, df):
    
    '''
    Takes in a variance, x (float between 0 and 1) and a DataFrame.  Drops columns
    having more than x percent of it's values missing.
    '''
    
    if 0 > x or x > 1:
        return "Error!  The value of x needs to be between 0 and 1"
    
    # Establish the percentage of missing values in each column
    percent_missing = df.isnull().sum()*100/len(df)
    percent_missing = percent_missing[percent_missing > x] # Keep only columns over x
    
    cols_to_drop = [col for col in percent_missing.index] # Create a list of column names
    df_transformed = df.drop(cols_to_drop, axis = 1) # Drop selected column names
    
    return df_transformed




def drop_correlated(x, df):
    
    '''
    Takes in a variance, x (float between 0 and 1) and a DataFrame.  Drops one of
    a pair of columns having more than x percent correlation.
    '''
    
    df_corr = df.corr().abs() # Calculate correlation matrix, save absolute values
    
    ind = np.where(df_corr > x) # Track the indices where correlation greater than x
    ind = [(df_corr.index[x], df_corr.columns[y])
          for x, y in zip(*ind) if x != y and x < y]
    
    for i in ind: # try except block to deal with potential KeyErrors
        try:
            df.drop(i[1], axis = 1, inplace = True)
        except KeyError:
            pass
    
    return df