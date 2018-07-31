# 圓周長：半徑 * 2 * pi
# 園面積：半徑 * 半徑 * pi
import math;
import uuid;

# function 
def calcPerimeter(r):
    return r * 2 * math.pi

def calcArea(r):
    return r * r * math.pi

print("圓周長:{:.2f}".format(calcPerimeter(100)))
print("圓面積:{:.2f}".format(calcArea(100)))

name = "Jack"
age = 20
def sayHi():
    print("Hello All, My Name is {},{}歲".format(name, age))

def register():
    return uuid.uuid1();

sayHi()
print("id:{}".format(register()))