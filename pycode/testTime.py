import time
import pandas as pd
import numpy as np


def do_something_with(item):
    list1.append(item)


data = pd.read_csv("../resultDataset/web_Google.csv")
# data = pd.read_csv("../resultDataset/facebook_combined2.csv")
item_list = np.unique(data.iloc[:, 0].append(data.iloc[:, 1])).tolist()
list1 = []
list2 = []

result = []

start = time.perf_counter()
result = (list1.append(item) for item in item_list)
end = time.perf_counter()
mytime1 = end - start
print("列表解析+生成器推荐方式的程序执行时间为：", mytime1)

start = time.perf_counter()
for item in item_list:
    list2.append(item)
end = time.perf_counter()
mytime2 = end - start
print("for循环方式的程序执行时间为：", mytime2)

print("reduce是否比for循环快：", mytime1 < mytime2)

print("list1 is ", list1)

# print("list2 is ",list2)
