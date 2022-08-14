#%%
import pandas as pd
import numpy as np
#from manim import *

# %%
#import CSV file
url='https://raw.githubusercontent.com/morey-ow/vlad-weather/main/dfRaw.csv'
df = pd.read_csv(url)
df=df.drop(['Unnamed: 0','wdir', 'pres', 'tsun'], axis=1)
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
  #      'wdir': 'Wind Direction Degrees (°)',
        'wspd': 'Wind Spd (km/h)', 
        'wpgt': 'Peak Wind Gust (km/h)',
  #      'pres': 'Sea-Level Pressure (hPa)', 
  #      'tsun': 'Daily Sunshine (mins) '
   })
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
date_column=df.pop('Date')
df.insert(0,'Date', date_column)
df

# %%
#df
# %%
#import dtale
#x=dtale.show(df)
#print(x.main_url()) #url where dtale gui loads
# %%
#add year column and month column
df['Year']=df['Date'].apply(lambda d: d.year)
df['Month']=df['Date'].apply(lambda d: d.month)
# %%
df_grouped=df.groupby(['Year', 'Month']).mean().reset_index()
df_grouped.head()
# %%
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('MacOSX')


df_grouped.plot(y='Avg Temp (°F)')
#plt.savefig()
plt.show()
# %%
import numpy as np
# %%
def least_squares(X,b):
    return np.linalg.inv(X.T@X)@X.T@b

# %%
#check our least squares can disc y=2x+1
X=np.array([0,1, 2, 1]).reshape(2,2)
b=np.array([1,5]).reshape(2,1)
least_squares(X, b)

# %%#
#find the best sinusoidal function predicting 
#average temperature
p=2*np.pi/12 #period is 1 year
# a cos px + b sin px +c is a sinusoidal
#x=np.array(df_grouped.index)
x=df_grouped.index
y=df_grouped['Avg Temp (°F)']
plt.scatter(x,y, color='blue')

X=np.array([np.cos(p*x), np.sin(p*x), np.ones(len(x))]).T
y=df_grouped['Avg Temp (°F)']
coefficients = least_squares(X,y) #= [a,b,c]
y_pred=X@coefficients

plt.plot(x, y_pred, c='red', label='sinusoidal')
plt.show()
# %%
import bokeh
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
output_notebook()
myfigure=figure(match_aspect=True, aspect_scale=1) #create a figure using figure from bokeh.plotting module
myfigure.line(x,y, size=30, color='red')
myfigure.line(x,y)
show(myfigure)
# %%
