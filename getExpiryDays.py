# importing datetime module
import datetime
# importing relativedelta, MO from dateutil
from dateutil.relativedelta import relativedelta, MO,TU,WE,TH,FR,SU

# getting today's date
todayDate = datetime.date.today()
print('Today Date:',todayDate)

# Increment today's date with 1 week to get the next Monday
# nextMonday = todayDate + datetime.timedelta(days=-todayDate.weekday(), weeks=1)
nextSunday = todayDate + relativedelta(weekday=SU(1))
nextMonday = todayDate + relativedelta(weekday=MO(1))
nextTuesday = todayDate + relativedelta(weekday=TU(1))
nextWednesday = todayDate + relativedelta(weekday=WE(1))
nextThursday = todayDate + relativedelta(weekday=TH(1))
nextFriday = todayDate + relativedelta(weekday=FR(1))
print('Next Sunday Date:',nextSunday)
print('Next Monday Date:',nextMonday)
print('Next Tuesday Date:',nextTuesday)
print('Next Wednesday Date:',nextWednesday)
print('Next Thursday Date:',nextThursday)
print('Next Friday Date:',nextFriday)

print(type(nextMonday))
# lastMonday = todayDate + relativedelta(weekday=MO(-1))

# printing the last Monday date
#print("The last Monday date:", lastMonday)

# Pass MO(1) as an argument to relativedelta to set weekday as Monday and 1 signifies next week's Monday
# nextMonday = todayDate + relativedelta(weekday=TU(1))

# printing the Next Monday date
# print("The Next Monday date:", nextMonday)