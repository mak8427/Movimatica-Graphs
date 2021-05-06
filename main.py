import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime,timedelta
import numpy as np
import operator


df=pd.read_csv('posizioni (2).csv')
df=df.rename(columns={'Data [dd.MM.yy HH:mm:ss]':'Date','Longitudine':'Longitude','Latitudine':'Latitude','Indirizzo':'Address','Luogo':'City','CAP':'ZIP','Velocità':'Velocity','Tipo':'Type'})
df['Date']=pd.to_datetime(df.Date, format="%d.%m.%y %H:%M:%S")
#mean time of refresh for the position
Mean=0
i=1
sum=0
ping_list=[]
while i<len(df):
    timedifference=df['Date'][i]-df['Date'][i-1]
    min15=timedelta(minutes=15)
    sec2=timedelta(seconds=2)
    if timedifference<=min15 and timedifference>=sec2:#removing the offline time from online and offline stance
      timedelta_seconds = timedifference.total_seconds()
      ping_list.append(int(timedelta_seconds))
    i=i+1
unique, counts = np.unique(ping_list, return_counts=True)
counts=dict(zip(unique, counts))
mean=np.mean(ping_list)
counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}

print('the most frequent time of response is '+str(list(counts)[-1])+' with '+str(counts.get(int(list(counts)[-1])))+'occurrences')
print('the minimum time of response is '+str(timedelta(seconds=min(ping_list))))
print('the maximum time of response is '+str(timedelta(seconds=max(ping_list))))
print('the average time of response is '+str(timedelta(seconds=round(mean))))
plt.hist(ping_list,range=(0,350),bins=350)
plt.show()


