import numpy as np
import pygrib # import pygrib interface to grib_api

import pandas as pd

year = 2018

grbs = pygrib.open('data/weather_copernicus_TMA_grib_2018/copernicus_TMA_precipitation_2018.grib')

#with open("copernicus_TMA_precipitation_2018.txt", "w") as text_file:
#    for grb in grbs:
#        print("{} {} {} {} {}#\n".format(grb.typeOfLevel,grb.level,grb.name,grb.shortName,grb.parameterUnits), file=text_file)
#    print("{}\n".format(grb.keys()), file=text_file)

#grbs.rewind() # rewind the iterator

my_y1 = 59
my_y2 = 61
my_x1 = 17
my_x2 = 19


new_data = []

import time
from calendar import monthrange

start_time = time.time()

for m in range(1,13):
    
    number_of_days = monthrange(year, m)[1]
    
    for d in range(1,number_of_days+1):
        
        for h in range(0,24):
            
            # No data for all hours
            
            selected_grbs=np.array(grbs.select(name='Total precipitation', month=m, day=d, hour=h, minute=0, second=0))
            precipitation=selected_grbs[0].data(lat1=my_y1,lat2=my_y2,lon1=my_x1,lon2=my_x2)
            
            selected_grbs=np.array(grbs.select(name='Precipitation type', month=m, day=d, hour=h, minute=0, second=0))
            precipitation_type=selected_grbs[0].data(lat1=my_y1,lat2=my_y2,lon1=my_x1,lon2=my_x2)

            print(m, d, h)
            
            for lat_idx in range(8,-1,-1):
                for lon_idx in range (8,-1,-1):
                    new_d = {}
                    new_d['month'] = m
                    new_d['day'] = d
                    new_d['hour'] = h
                    new_d['lat'] = precipitation[1][lat_idx][0]
                    new_d['lon'] = precipitation[2][0][lon_idx]
                    new_d['precipitation'] = precipitation[0][lat_idx][lon_idx]
                    new_d['precipitation_type'] = precipitation_type[0][lat_idx][lon_idx]
            
                    new_data.append(new_d)

data_df = pd.DataFrame(new_data, columns = ['month', 'day', 'hour', 'lat', 'lon', 'precipitation', 'precipitation_type'])

data_df.to_csv("data/weather_copernicus_TMA_csv_2018/copernicus_TMA_precipitation_2018.csv", sep=' ', encoding='utf-8', float_format='%.6f', header=True, index=False)

print((time.time()-start_time)/60)
