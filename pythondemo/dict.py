# {key:value,key:value....}
x = {"name":"Jack","age":30}
# print(type(x))

#讀取資料
# dict["key"] -> value
# print(x["name"])
# print(x["age"])

#新增或修改
# x["age"] = 40
# x["email"] = "Jack@gmail.com"

#刪除
# del x["age"]
# print(x)

# print("email" in x) #False

#迴圈
# for k in x:
#     print(k, x[k])  #name、age

# for k in x.keys():
#     print(k)
# for v in x.values():
#     print(v)
# for k,v in x.items():
#     print(k,v)

# print(x.get("name"))
print(x.pop("name"))
print(x)
