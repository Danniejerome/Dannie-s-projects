import pytz
from datetime import datetime
# time_zones = pytz.all_timezones
# print(time_zones)
country_name = pytz.timezone('Asia/Delhi')
country_time = datetime.now(country_name)
print(country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))
