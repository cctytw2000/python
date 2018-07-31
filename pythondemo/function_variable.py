# def fun():
#     print(var)      #5
# var = 5
# fun()
# print(var)          #5

# def fun():
#     var = 10
#     print(var)      #10
# var = 5
# fun()
# print(var)          #5

def fun():
    global var
    var = 10
    print(var)      #10
var = 5
fun()
print(var)          #10