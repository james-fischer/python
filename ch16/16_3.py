import copy

class Time(object):
    """Represents a time in hours, minutes, and seconds.
    """

def print_time(Time):
    print("%.2d: %.2d: %.2d" %(Time.hour, Time.minute, Time.second))


def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

def secs(Time):
    return Time.hour*3600 + Time.minute*60 + Time.second



def increment(Time, seconds):
    
    newTime = copy.deepcopy(Time)

    initial = secs(Time)
    total = initial + seconds

    hours = total//3600
    rem = total%3600

    minutes = rem//60
    sec = rem%60

    newTime.hour = hours
    newTime.minute = minutes
    newTime.second = sec
    
    return newTime



#Main


myTime = Time()
myTime.hour = 1
myTime.minute = 1
myTime.second = 1

newTime = increment(myTime, 9999)
print_time(newTime)

"""
start = Time()
start.hour = 9
start.minute = 45
start.second = 0


duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0


done = add_time(start, duration)
print_time(done)
"""
