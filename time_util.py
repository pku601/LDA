import time
import datetime


def Caltime(date1, date2):
    date1 = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2 = time.strptime(date2, "%Y-%m-%d %H:%M:%S")
    date1 = datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
    date2 = datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
    return date2 - date1


def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
