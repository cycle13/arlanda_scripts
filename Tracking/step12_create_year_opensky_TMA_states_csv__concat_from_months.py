import pandas as pd
import os

import time
start_time = time.time()

year = '2018'
DATA_DIR = os.path.join("data", "states_TMA_opensky_merged_with_ddr_m3_" + year)

months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

frames = []
#opensky_states_df = pd.DataFrame(columns=['flightId', 'sequence', 'timestamp', 'lat', 'lon', 'altitude', 'velocity', 'endDate', 'aircraftType'])

for month in months:
    print(month)    

    filename = 'states_TMA_opensky_' + year + '_' + month + '.csv'
    
    df = pd.read_csv(os.path.join(DATA_DIR, filename), sep=' ', names = ['flightId', 'sequence', 'timestamp', 'lat', 'lon', 'altitude', 'velocity', 'endDate', 'aircraftType'],
                     dtype = str)
     
    frames.append(df)

opensky_states_df = pd.concat(frames)

filename = 'states_TMA_opensky_' + year + '.csv'
opensky_states_df.to_csv(os.path.join(DATA_DIR, filename), sep=' ', encoding='utf-8', float_format='%.6f', index=False, header=None)

print((time.time()-start_time)/60)
