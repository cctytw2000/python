# a = {}   #dict
# a = set()

my_set = {30,"Tom","Tom@gmail.com"}

#新增
# my_set.add(31)
# my_set.add(30)  #不會再加入
# my_set.update(["02-11112222","0911222333"])

#刪除
# my_set.discard(30)
# my_set.remove(30)
# print(my_set.pop())
# print(my_set)



set_a = {2,4,6,8,10,12}
set_b = {3,6,9,12}

#取得所有元素-聯集
# print(set_a.union(set_b))
# print(set_a | set_b)

#取得集合中重複的元素-交集
# print(set_a.intersection(set_b))
# print(set_a & set_b)
#取出set_a中跟set_b不一樣的元素 - 差集
print(set_a.difference(set_b))
print(set_a - set_b)
#取出set_b中跟set_a不一樣的元素 - 差集
print(set_b.difference(set_a))
print(set_b - set_a)

#取出set_a與set_b中不一樣的元素 - 對稱差
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)
