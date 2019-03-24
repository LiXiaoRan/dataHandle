import numpy as np
import pandas as pd
import scipy
from scipy.io import loadmat
import csv


def trans(FILENAME):
    _CSV = ".csv"
    # 读取文件的文件夹路径
    FILEINNAME = '../dataset/'
    # 结果文件的文件夹路径
    FILEOUTNAME = '../resultDataset/'

    # 读取文件的路径
    FILEINPATH = FILEINNAME + FILENAME + _CSV
    # 结果文件的路径
    FILEOUTPATH = FILEOUTNAME + FILENAME + _CSV

    csvFile = open(FILEINPATH, "r")
    csvoutFile = open(FILEOUTPATH, "w", newline='')

    reader = csv.reader(csvFile)
    writer = csv.writer(csvoutFile)

    list = []
    for item in reader:
        result = item[0].split(' ')
        if result[0] != result[1] and int(result[0]) != (int(result[1]) + 1):  # 这里and后面只是针对fe_4elt2这个数据设置的判断条件
            list_item = {'source': result[0], 'target': result[1]}
            print(list_item)
            list.append(list_item)

    for item in list:
        w_row = [item['source'], item['target']]
        writer.writerow(w_row)


trans('fe_4elt2')
