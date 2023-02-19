#1
from datetime import date, timedelta, datetime, time

d = date.today() - timedelta(5)

print('5 days ago:', d)


#2
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)
print(f"yesterday: {yesterday}, today: {date.today()}, tomorrow: {tomorrow}")


#3
d = datetime.today().ctime()
dt = datetime.today().replace(microsecond=0)

print(f"{d} \nor \n{dt}")


#4

def difference(dt2, dt1):
  td = dt2 - dt1
  return td.days * 24 * 3600 + td.seconds


d2 = datetime.now()
d1 = datetime.strptime('2023-02-15 15:04', '%Y-%m-%d %H:%M')


print("\n%d seconds" % (difference(d2, d1)))
