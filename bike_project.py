import pandas as pd
import numpy as np
    
# class TripDataPrep(self, ):

def r_w_bike_trips(path, location_name, num_shops, app_token, limit=50000, offset=50000):
    '''
    Reads an API accessible dataset given url path and other url call variables.
    Writes out to a json file

    Parameters:
    -----------
    path (str): url path beginning with https:
    location_name (str): name to assign to the trip counts column
    token (str): app_token
    limit (int): max rows to request
    offset (int): starting point for gathering rows

    Output:
    --------
    json-formatted file named 'location_name.json'
    '''
    df_a = pd.read_json( f'{path}?$limit={limit}&$offset={0}&$$app_token={app_token}')
    df_b = pd.read_json( f'{path}?$limit={limit}&$offset={offset}&$$app_token={app_token}')
    df = df_a.append(df_b)    
    # rename trip_count column to location_name
    df[location_name] = df.iloc[:, -2:].sum(axis=1)
    df[location_name].fillna(0, inplace=True) 
    
    # calculate date, month, year, dow, commuter (boolean), trip count am peak, trip count other times
    df['short_date'] = pd.DatetimeIndex(df['date']).date
    df['month'] = pd.DatetimeIndex(df['date']).month
    df['year'] = pd.DatetimeIndex(df['date']).year
    df['dow'] = pd.DatetimeIndex(df['date']).dayofweek
    df['hour'] = pd.DatetimeIndex(df['date']).hour
    df['am_commuter'] = df['dow'].isin([0,1,2,3,4]) & (df['hour'].isin([5,6,7,8,9]))
    df[f'{location_name}_am_peak'] = np.where(df['am_commuter']==True, df[location_name], 0)
    df[f'{location_name}_other'] = np.where(df['am_commuter']==False, df[location_name], 0)
    
    # collapse table by date and create sum counts for commuter and (other-(2 x commuter))
    df_by_date = df.groupby(['short_date', 'month', 'year', 'dow']).agg(
                                        {f'{location_name}_am_peak':'sum',
                                         f'{location_name}_other':'sum'
                                          }).reset_index()
    
    # commuters travel 2 ways--remove assumed pm commuter trips from trip count other
    df[f'{location_name}_other'] = df[f'{location_name}_other'] - df[f'{location_name}_am_peak']
    
    # add in count of nearby bike shops
    df_by_date[f'{location_name}_bike_shops'] = num_shops
    df_by_date.to_json(f'data/{location_name}.json', date_format='iso')
    
    #test output to be sure the read operation went ok
    print(df_by_date.head())


def merge_counter_locations(location_dict):
    '''
    Loops through a dict of counter locations, creating a json file path for each 
    location and merging counter files by date to create a master bike trip
    count file with 'am_peak' and 'other' bike trips for each location for each day.

    Parameters:
    ----------
    location_dict (dict): dict with root names of json files

    Returns:
    -------
    df (dataframe): master bike trip count file
    '''
    count = 1
    for k,v in urls.items():
        if count == 1:
            df = pd.read_json(f'data/{k}.json')
        else:
            df_next = pd.read_json(f'data/{k}.json')
            df = df.merge(df_next, how="left", left_on=["short_date", "month", "year", "dow"], right_on=['short_date', "month", "year", "dow"])
        count += 1
    df['date'] = pd.DatetimeIndex(df['short_date']).date
    return df


def add_weather(df, weather_file, keep_cols):
    '''
    Reads in daily weather data from a NOAA-generated source and merges it
    into a dataframe by date
    Parameters:
    ----------
    df (dataframe): destination dataframe
    weather_file (.csv): source weather .csv file
    keep_cols (list): list of weather attributes to keep

    Returns:
    -------
    Updated dataframe
    '''
    df_seattle_weather = pd.read_csv(weather_csv, usecols=keep_cols)
    df_seattle_weather['date'] = pd.DatetimeIndex(df_seattle_weather["DATE"]).date
    df = df.merge(df_seattle_weather, how="left", left_on="date", right_on='date')
    df.index = df['date']
    return df
    
    
def add_daily_summary_data(df, bike_shops_d):
    '''
    Adds daily summary statistics for trip counts
    Parameters:
    ----------
    df (dataframe): pandas table of bike counts by station
    bike_shops_d (dict): dict with number of bike shops in vicinity of bike trip counter location
    
    Returns:
    -------
    df (dataframe): df with summary statistics added
    '''
    few_am_peak, many_am_peak, few_other, many_other = [], [], [], []

    for k,v in bike_shops.items():
        if v <= 3:
            few_am_peak.append('{}_am_peak'.format(k))
            few_other.append(f'{k}_other')
        else:
            many_am_peak.append(f'{k}_am_peak')
            many_other.append(f'{k}_other')

    df['few_am_peak_ttl'] = df[few_am_peak].sum(axis=1)
    df['many_am_peak_ttl'] = df[many_am_peak].sum(axis=1)
    df['few_other_ttl'] = df[few_other].sum(axis=1)
    df['many_other_ttl'] = df[many_other].sum(axis=1)
    df['am_peak_ttl'] = df['few_am_peak_ttl'] + df['many_am_peak_ttl']
    df['other_ttl'] = df['few_other_ttl'] + df['many_other_ttl']
    return df