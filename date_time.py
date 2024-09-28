#to get a current date and time whe need to use datetime librery
from datetime  import datetime

current_date = datetime.now()
# the now function returns a datetime object
print('tody is :' + str(current_date))

#THERE ARE FUNCTIONS THAT YOU CAN USE WITH DATETIME OBJECT TO MANUPILATE DATES

from datetime import datetime, timedelta
today = datetime.now()
print('today is: '+ str(today))


#timedelta is used to defined a periode of time

one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was:' + str(yesterday))

#use date functions to control date formatting
from datetime import datetime
current_date = datetime.now()


print('day: ' + str(current_date.day))
print('month: ' + str(current_date.month))
print('year: ' + str(current_date.year))

one_year = timedelta(days=365)
last_year = today - one_year
print('last year was:' + str(last_year))

#sometime    you receive  a the date as string and tou want to convert it to a datetime object
from datetime import datetime

birthday  = input('When is your birthday(dd/mm/yyyy)?')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print('Birthday: ' + str(birthday_date))

# converting it to a datetime allows you to use the date functions
from datetime import datetime

birthday =  input('When is your birthday (dd/mm/yyy)?')

birthday_date = datetime.strptime(birthday,  '%d/%m/%y')
print('Birthday:'+ str(birthday_date))

one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day  befor birthday: ' + str(birthday_eve))