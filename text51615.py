import datetime
import time
a = datetime.datetime.now()
b = time.strftime("%Y-%m-%d %H:%M", time.localtime())
d = datetime.datetime(b)
c = b
print(d)
print(type(d))

print(a)
print(type(a))
