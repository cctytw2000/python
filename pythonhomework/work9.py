# 9.	讓使用者輸入身高、體重、腰圍及性別
# 根據身高及體重算出BMI，18.6 >= BMI < 24，或男性腰圍<90、女性腰圍<80，
# 就列印出健康，否則就列印出不健康，請使用function來完成
bf   = input("請輸入性別(男OR女):")
tall =  int(input("請輸入身高:"))
fat  =  int(input("請輸入體重:"))
heavy = int(input("請輸入腰圍:"))
bmi  = fat / (tall / 100 ) ** 2
def myself():
    if bf == "男" :
        if bmi >=18.6 and bmi < 24 and heavy < 90:
            print("健康")
        else :
            print("不健康")
    if bf == "女" :
        if bmi >=18.6 and bmi < 24 and heavy < 80:
            print("健康")
        else :
            print("不健康")
myself()
     




   