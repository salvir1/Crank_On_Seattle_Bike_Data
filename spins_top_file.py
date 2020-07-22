import numpy as np
import pandas as pd
import bike_project as bp
import json

urls = {
        'Ballard' : 'https://data.seattle.gov/resource/47yq-6ugv.json',
        'Capitol_Hill' : 'https://data.seattle.gov/resource/j4vh-b42a.json',
        'Central_2nd_Ave' : 'https://data.seattle.gov/resource/avwm-i8ym.json',
# no data until 2019        'Central_7th_Ave' : 'https://data.seattle.gov/resource/qfzg-zmyj.json', 
        'West_Seattle' : 'https://data.seattle.gov/resource/mefu-7eau.json',
        'I90_lid' : 'https://data.seattle.gov/resource/u38e-ybnc.json',
        'NE_Seattle' : 'https://data.seattle.gov/resource/2z5v-ecg8.json',
        'Myrtle_Edwards' : 'https://data.seattle.gov/resource/4qej-qvrz.json'
        }

bike_shops = {
        'Ballard' : 3,
        'Capitol_Hill' : 2,
        'Central_2nd_Ave' : 5,
        'Central_7th_Ave' : 6,
        'West_Seattle' : 3,
        'I90_lid' : 5,
        'NE_Seattle' :6 ,
        'Myrtle_Edwards' : 3
}

limit = 30000
offset = 30000

with open('data/app_token.txt', 'r') as t_file: 
    app_token = t_file.read() 

for k, v in urls.items():
    r_w_bike_trips(v, k, bike_shops[k], app_token, limit, offset)