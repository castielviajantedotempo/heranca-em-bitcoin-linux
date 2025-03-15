import time
from datetime import datetime

####### Main
def days():
    timestr = "20081031-164121"

    current_time = time.strftime("%Y%m%d-%H%M%S")
    date_format = '%Y%m%d-%H%M%S'
    d1 = datetime.strptime(current_time, date_format)
    d0 = datetime.strptime(timestr, date_format)

    delta = d1 - d0
    #print(delta.days)
    return delta.days
