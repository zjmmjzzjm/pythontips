# pip3 install pytz
import pytz
from datetime import datetime
import time
#print(pytz.all_timezones)

# date +%s
# timestamp <-> datetime

ts = 1585670057
print (ts)
tz  = pytz.timezone('UTC')
tz1  = pytz.timezone('Asia/Shanghai')
tz2 = pytz.timezone('US/Eastern')
dtt = datetime.fromtimestamp(ts, tz)
dtt1 = datetime.fromtimestamp(ts, tz1)
dtt2 = datetime.fromtimestamp(ts, tz2)
print( dtt, tz)
print( dtt1, tz1)
print( dtt2, tz2)

new_dtt = datetime.strptime('2020-03-31 15:54:17', '%Y-%m-%d %H:%M:%S')
new_dtt1 = datetime.strptime('2020-03-31 23:54:17', '%Y-%m-%d %H:%M:%S')
new_dtt2 = datetime.strptime('2020-03-31 11:54:17', '%Y-%m-%d %H:%M:%S')
ts = tz.localize(new_dtt).timestamp()
ts1 = tz1.localize(new_dtt1).timestamp()
ts2 = tz2.localize(new_dtt2).timestamp()
print(ts, tz)
print(ts1, tz1)
print(ts2, tz2)


new_dtt = datetime.strptime('2020-03-31 15:54:17', '%Y-%m-%d %H:%M:%S')
new_dtt1 = datetime.strptime('2020-03-31 23:54:17', '%Y-%m-%d %H:%M:%S')
new_dtt2 = datetime.strptime('2020-03-31 11:54:17', '%Y-%m-%d %H:%M:%S')
ts = new_dtt.replace(tzinfo=tz).timestamp()
ts1 = new_dtt1.replace(tzinfo=tz1).timestamp()
ts2 = new_dtt2.replace(tzinfo=tz2).timestamp()
print(ts,new_dtt,  tz)
print(ts1,new_dtt1, tz1)
print(ts2, new_dtt2, tz2)




