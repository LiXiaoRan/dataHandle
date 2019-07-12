import random
import numpy as np
import csv

# 生成一些的测试数据

_CSV = ".csv"


def generate(FileName):
    RESULT_PATH = "../testRandomData/"
    FileHeader = "AMVegaData_"

    OUT_FILE = RESULT_PATH + FileHeader + FileName + _CSV
    # recordFile = open(OUT_FILE, 'a')
    csvoutFile = open(OUT_FILE, "w", newline='')
    writer = csv.writer(csvoutFile)

    writer.writerow(['Layout', 'Aesthetic Metric', 'Metric Value'])

    AMlist = ['Noack', 'Crosslessness', 'Minimum angle metric', 'Edge length variation']
    LayoutList = ['My', 'Yifan Hu', 'OpenOrd', 'Fruchterman-Reingold']

    for am in AMlist:
        for ll in LayoutList:
            if am == 'Noack':
                w_row = [ll, am, np.random.uniform() + 1.0]
                writer.writerow(w_row)
            elif am == 'Edge length variation':
                w_row = [ll, am, np.random.uniform() / 10.0]
                writer.writerow(w_row)
            else:
                w_row = [ll, am, np.random.uniform()]
                writer.writerow(w_row)


FileNameList = ['cit-HepTh', 'twitter', 'web-Google']

for item in FileNameList:
    generate(item)
