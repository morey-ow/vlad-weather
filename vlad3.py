#%%
import pandas as pd
import numpy as np
from manim import *

# %%
#import CSV file
df = pd.read_csv('dfRaw.csv')
del df['Unnamed: 0']
df
# %%
df.columns
# %%
df = df.rename(columns={
        'date': 'Date', 
        'tavg': 'Avg Temp (°C)', 
        'tmin': 'Min Temp (°C)', 
        'tmax': 'Max Temp (°C)', 
        'prcp': 'Precipitation (mm)', 
        'snow': 'Snow (mm)',
        'wdir': 'Wind Direction Degrees (°)',
        'wspd': 'Wind Spd (km/h)', 
        'wpgt': 'Peak Wind Gust (km/h)',
        'pres': 'Sea-Level Pressure (hPa)', 
        'tsun': 'Daily Sunshine (mins) '})
# %%
# convert Date column to datetime object
from datetime import datetime

df['Date']=pd.to_datetime(df['Date'])
df.dtypes
# %%
#df[df.columns[1:4]]=df[df.columns[1:4]].apply(lambda s: 9*s/5 +32)
C_to_Fdict=   {
     'Avg Temp (°C)':'Avg Temp (°F)', 
     'Min Temp (°C)':'Min Temp (°F)',
     'Max Temp (°C)':'Max Temp (°F)'
     }
df_Ftemps=df[C_to_Fdict.keys()].apply(lambda s:9*s/5 + 32)
df_Ftemps.columns=C_to_Fdict.values()
print(df_Ftemps)

# %%
df.drop(columns=C_to_Fdict.keys(), inplace=True)
df=pd.concat([df_Ftemps,df], axis=1)
print(df)

# %%
#move date column to front
data_column=df.pop('Date')
df.insert(0,'Date', data_column)

# %%
df
# %%
import dtale
dtale.show(df)
# %%
