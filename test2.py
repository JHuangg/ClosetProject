import socket
import sys
import time
from datetime import datetime, timedelta
import sched

laser_state = 0

while True:

    temp = 0
    starttime = time.time()
    while True:
        print("testing")
        time.sleep(5.0 - ((time.time() - starttime) % 5.0))
