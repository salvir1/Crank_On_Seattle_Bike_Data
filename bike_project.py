import pandas as pd
    
# class TripDataPrep(self, ):

def read_bike_trips(source, location_name, token, limit=50000, offset=50000, date='date'):
    df = pd.read_json('https://data.seattle.gov/resource/47yq-6ugv.json?$limit=30000&$offset=30001&$$app_token=GphdTjjI7akvPvXuiP95RpyI3')
    return df

def gen_date_time():
    pass

def split_into_commuter_noncommuter():

pass


