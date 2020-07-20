import pandas as pd
    
# class TripDataPrep(self, ):

def read_bike_trips(path, location_name, token, limit=50000, offset=50000):
    '''
    Reads an API accessible dataset given url path and other url call variables
    Parameters:
    -----------
    path (str): url path beginning with https:
    location_name (str): name to assign to the trip counts column
    token (str): app_token
    limit (int): max rows to request
    offset (int): starting point for gathering rows

    Returns:
    --------
    pandas dataframe
    '''

    df = pd.read_json( f'{path}?$limit={limit}&$offset={offset}&$$app_token={app_token}')


def gen_date_time(df):
    '''
    Generates date/time variables from the single date variable.
    Parameters:
    -----------
    df: pandas dataframe

    Returns:
    --------
    df: Pandas dataframe with new date-coded columns
    '''

    df['month'] = pd.DatetimeIndex(df['date']).month
    df['year'] = pd.DatetimeIndex(df['date']).year
    df['dow'] = pd.DatetimeIndex(df['date']).dayofweek
    df['hour'] = pd.DatetimeIndex(df['date']).hour
    df['am_commuter'] = df['dow'].isin([7,1,2,3,4]) & (df['hour'].isin([5,6,7,8,9]))
    am_commuter_group = (df[df['am_commuter'] == True])


def split_into_commuter_noncommuter():
    pass


