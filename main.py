import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime,timedelta
import numpy as np
import operator


df=pd.read_csv('posizioni (1).csv')
df=df.rename(columns={'Data [dd.MM.yy HH:mm:ss]':'Date','Longitudine':'Longitude','Latitudine':'Latitude','Indirizzo':'Address','Luogo':'City','CAP':'ZIP','Velocità':'Velocity','Tipo':'Type'})
df['Date']=pd.to_datetime(df.Date, format="%d.%m.%y %H:%M:%S")

#mean time of refresh for the position
Mean=0
i=1
sum=0
ping_list=[]
while i<len(df):
    timedifference=df['Date'][i]-df['Date'][i-1]
    min15=timedelta(minutes=2)
    sec2=timedelta(seconds=1)
    if timedifference<=min15 and timedifference>=sec2:#removing the offline time from online and offline stance
      timedelta_seconds = timedifference.total_seconds()
      ping_list.append(int(timedelta_seconds))
    i=i+1
unique, counts = np.unique(ping_list, return_counts=True)
counts=dict(zip(unique, counts))
mean=np.mean(ping_list)
counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}

print('the most frequent time of response is '+str(list(counts)[-1])+' with '+str(counts.get(int(list(counts)[-1])))+' occurrences')
print('the minimum time of response is '+str(timedelta(seconds=min(ping_list))))
print('the maximum time of response is '+str(timedelta(seconds=max(ping_list))))
print('the average time of response is '+str(timedelta(seconds=round(mean))))
plt.figure()
plt.hist(ping_list,range=(0,350),bins=350)
plt.show()
plt.close()
plt.figure()
sns.violinplot(x=ping_list)
plt.show()
plt.close()
#visualize position
address=df.iloc[1]['Address']
timedate=df.iloc[1]['Date']
print(address)
time_per_address={}
i=0
list_of_address=[df.iloc[1]['Address']]
alpha=False
while i<len(df):
    if df.iloc[i]['Address']!=address or i==len(df)-1:

        for ad in list_of_address:
            if ad == df.iloc[i]['Address']:
                timedelta_minutes = df.iloc[i]['Date'] - timedate
                timedate = df.iloc[i]['Date']
                address = df.iloc[i]['Address']
                timedelta_minutes = round(timedelta_minutes.total_seconds() / 60, 1)
                time_per_address[df.iloc[i-1]['Address']] =round(time_per_address.get(df.iloc[i]['Address'])+timedelta_minutes,2)
                alpha=True

        if alpha==False:
           timedelta_minutes=df.iloc[i]['Date']-timedate
           print(timedelta_minutes)
           timedate=df.iloc[i]['Date']
           address=df.iloc[i]['Address']
           timedelta_minutes=round(timedelta_minutes.total_seconds()/60,1)
           time_per_address[df.iloc[i-1]['Address']]=timedelta_minutes
        if df.iloc[i]['Address'] not in list_of_address:
          list_of_address.append(df.iloc[i]['Address'])



        alpha=False
    i=i+1
print(list_of_address)
print(time_per_address)
plt.figure()

plt.bar(height=time_per_address.values(), x=time_per_address.keys())
plt.show()

