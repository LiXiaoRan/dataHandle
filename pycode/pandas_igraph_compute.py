import pandas as pd
import numpy as np
from igraph import *
import csv
from multiprocessing.dummy import Pool as ThreadPool


def construce_graph(item):
    # print(FILE_NAME, " 开始构建边")

    print("construce_graph item is ", item)

    # source = nodes.index(item[0])
    # target = nodes.index(item[1])
    # links.append((source, target))
    # print("添加边：", source, target)


nodes = []
links = []


def compute_cc(FILE_NAME):
    _CSV = ".csv"
    FILE_PATH = "../resultDataset/"
    FILE_OUT_PATH = "../igraph_result/" + FILE_NAME + "_cc" + _CSV

    data = pd.read_csv(FILE_PATH + FILE_NAME + _CSV, header=None)
    csvoutFile = open(FILE_OUT_PATH, "w", newline='')
    writer = csv.writer(csvoutFile)

    data0 = np.unique(data.iloc[:, 0].append(data.iloc[:, 1]))
    print("读取 ", FILE_NAME, " 文件完毕，一共 ", len(data0), " 节点 ", len(data), " 条边")
    print("节点列表 is ", data0)
    nodes = data0.tolist()
    print(FILE_NAME, " 开始构建添加边")
    for row in data.itertuples(index=False):
        links.append((nodes.index(row[0]), nodes.index(row[1])))

    # result = (links.append((row[0], row[1])) for row in data.itertuples(index=False))
    print(len(links))
    # result = []

    print(FILE_NAME, " 开始构建有向图")
    graph = Graph(directed=True)
    graph.add_vertices(len(nodes))
    graph.add_edges(links)
    print(FILE_NAME, " 有向图构建完毕")

    print(FILE_NAME, " 开始使用igraph计算，参数为：normalized=True,mode=ALL ")
    result = graph.closeness(normalized=True, mode=ALL)
    print(FILE_NAME, " 计算结束")
    print(FILE_NAME, " 结果开始存入文件")
    count = 0
    for node_id in nodes:
        print(node_id, result[count])
        writer.writerow([node_id, result[count]])
        count += 1

    csvoutFile.close()
    print(FILE_NAME, " 的结果成功存入文件")


compute_cc("web_Google")
