dict1 = {"小影":"小影2","吃饭":"没吃饱"}
print("小影",dict1["小影"])               #对应输入和打印的关系，在后面索引
dict1["花姑娘"] = "a213213"               #此形式可以直接添加   key:balue进到dict1的字典中
print(dict1)
dict2={}
dict2=dict2.fromkeys((1,2,3,4),"小影")   #fromkeys(,)前面定义key  后面统一为value   后面只为一个参数
#dict.keys    dict.values    这两个分别是导出字典dict的key值和value值   dict.items()  则是将字典里的key与vlue的值分别对应用元组的形式导出
print(dict2)
num = {1,2,3,4,5,1}          #   此时num为一个集合，集合里的数据是唯一的
set1 = set([1,2,3,4,5,1,2])   #  创建一个集合
# #剔除一个列表中重复的元素
# num1 =[0,1,2,3,4,5,5,3,1]        原有列表
# num1 = list(set(num1))        让列表变为一个集合的形式，进行数据唯一性的自动剔除   set（）创建一个集合   使用set（）所得集合是无序的
# print(num)  
a=frozenset([0,12,1,3,4,5])       #使用frozenset()定义不可变集合   此时a里是无法增加或删除参数的