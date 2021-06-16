from _datetime import datetime
import time

datetime.now().strftime('%d-%m-%Y %H:%M:%S')
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
while True:
    time.sleep(3)
    print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))