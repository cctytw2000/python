import math

class Circle:
    def __init__(self, r):
        #成員變數
        self.radius = r
    # 成員函式
    def calcPerimeter(self):
        return self.radius * 2 * math.pi

    def calcArea(self):
        return self.radius * self.radius * math.pi

#產生物件
circleA = Circle(100)
circleB = Circle(50)
#circleA.方法();
#circleA.屬性 = 100;
print("圓周長:{:.2f}".format(circleA.calcPerimeter()))
print("圓面積:{:.2f}".format(circleA.calcArea()))

print("圓周長:{:.2f}".format(circleB.calcPerimeter()))
print("圓面積:{:.2f}".format(circleB.calcArea()))
