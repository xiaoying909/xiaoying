import pickle         # 泡菜   导入和导出   二进制多注意
my_list=[1,2,3.14,'小影',['anorher list']]
pickle_file = open('my_list','wb')
pickle.dump(my_list,pickle_file)
pickle_file.close
pickle_file = open('my_list','rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)