import time
from datetime import datetime
import IsManAlive

####### Main
def sharp_time():
    while True:
        expected_hour = 10
        expected_minute = 00
        current_time = time.strftime("%Y%m%d-%H%M%S")
        date_format = '%Y%m%d-%H%M%S'
        d1 = datetime.strptime(current_time, date_format)
        times = d1.time()
        if times.hour == expected_hour:
            if times.minute == expected_minute:
                IsManAlive.main()
        time.sleep(60)

sharp_time()
