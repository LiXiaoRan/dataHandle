from igraph import *
import csv
import os



def compute_cc(FILE_NAME):
    _CSV = ".csv"
    FILE_PATH = "../resultDataset/"
    FILE_OUT_PATH = "../igraph_result/" + FILE_NAME + "_cc" + _CSV

    csvFile = open(FILE_PATH + FILE_NAME + _CSV, "r")
    csvoutFile = open(FILE_OUT_PATH, "w", newline='')

    reader = csv.reader(csvFile)
    writer = csv.writer(csvoutFile)

    print(FILE_NAME, " 文件读取完毕")

    graph = Graph(directed=True)

    nodes = []
    links = []

    print(FILE_NAME, " 开始构建有向图")
    for item in reader:
        if nodes.count(item[0]) == 0:
            nodes.append(item[0])
        if nodes.count(item[1]) == 0:
            nodes.append(item[1])

        source = nodes.index(item[0])
        target = nodes.index(item[1])
        links.append((source, target))
        print("添加边：",source, target)

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

    csvFile.close()
    csvoutFile.close()
    print(FILE_NAME, " 的结果成功存入文件")


compute_cc("fe_4elt2")
