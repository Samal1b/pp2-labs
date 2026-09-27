#1
import datetime

today=datetime.date.today() 
#print(today - datetime.timedelta(5))


#2
today=datetime.date.today()
yesterday=today-datetime.timedelta(1)
tomorrow=today+datetime.timedelta(1)

#print(yesterday,today,tomorrow)


#3
now=datetime.datetime.now()
print(now.replace(microsecond=0))


#4
today=datetime.date.today()
yesterday=today-datetime.timedelta(1)
print((today-yesterday).total_seconds())



