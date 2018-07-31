# x,y,z = "10",10,False
# # print(type(x))      #str
# # print(type(y))      #int
# # print(type(z))      #bool

# # print(x + y) #?? 20   1010  #TypeError: must be str, not int

# # print(x + str(y))    #1010
# # print(int(x) + y)    #20

# print(int(z))       #0
# a = True
# print(int(a))       #1

# print(bool(x))      #True
# print(bool(y))      #True
# b = 0
# print(bool(b))      #False
# c = ""
# print(bool(c))      #False

#Python會將下列物件視為False
#False、0、""、0.0、None、()、[]、{}

a = input("請輸入數字：")
b = 10
print(type(a))
print(type(b))
print(int(a) + b)  #??