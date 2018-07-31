# 循序結構
weight = int(input("請輸入體重(kg)："))
height = int(input("請輸入身高(cm)："))
height_m = height/100
bmi = weight / (height_m ** 2)
# print("您的BMI是：", bmi)
print("身高{2}，體重{1}，您的BMI是：{0:.1f}".format(bmi,weight,height));
# 選擇結構
# if(bmi >= 18.5 and bmi < 24):
#     print("aaa")
#     print("bbb")
#     print("標準")
# else:
#     print("ccc")
#     print("ddd")
#     print("不標準")

if (bmi < 18.5):
    print("BMI值為{0:.1f}，屬體重過輕".format(bmi))
elif (18.5 <= bmi and bmi < 24):
    print("BMI值為{0:.1f}，屬正常範圍".format(bmi))
elif (24 <= bmi and bmi < 27):
    print("BMI值為{0:.1f}，屬稍重".format(bmi))
elif (27 <= bmi and bmi < 30):
    print("BMI值為{0:.1f}，屬輕度肥胖".format(bmi))
elif (30 <= bmi and bmi < 35):
    print("BMI值為{0:.1f}，屬中度肥胖".format(bmi))
else:
    print("BMI值為{0:.1f}，屬重度肥胖".format(bmi))





