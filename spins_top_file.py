import numpy as np
import pandas as pd
import bike_project as bp

urls = {
        'Ballard' : 'https://data.seattle.gov/resource/47yq-6ugv.json',
        'Capitol_Hill' : 'https://data.seattle.gov/resource/j4vh-b42a.json',
        'Central_2nd_Ave' : 'https://data.seattle.gov/resource/avwm-i8ym.json',
#         'Central_7th_Ave' : 'https://data.seattle.gov/resource/qfzg-zmyj.json',
#         'West_Seattle' : 'https://data.seattle.gov/resource/mefu-7eau.json',
#         'I90_lid' : 'https://data.seattle.gov/resource/u38e-ybnc.json',
#         'NE_Seattle' : 'https://data.seattle.gov/resource/2z5v-ecg8.json',
#         'Myrtle_Edwards' : 'https://data.seattle.gov/resource/4qej-qvrz.json'
        }
limit = 30000
offset = 0

with open('data/app_token.txt', 'r') as t_file: 
    app_token = t_file.read() 

df = bp.read_bike_trips(urls['Ballard'], 'Ballard', app_token, limit, offset)
# for k, v in urls.items():
#     if k != 'Ballard':
#         df_ = df_.append(bp.read_bike_trips(v, k, app_token, limit, offset))