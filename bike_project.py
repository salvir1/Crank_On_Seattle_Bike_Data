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
    