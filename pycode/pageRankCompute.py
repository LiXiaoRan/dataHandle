import csv
import networkx as nx
import numpy as np
import pandas as pd

FILE_NAME = "web_NotreDame.csv"
FILE_PATH = "../resultDataset/"
FILEOUTPATH = FILE_PATH + "web_NotreDame_pg.csv"

graph = nx.DiGraph()

csvFile = open(FILE_PATH + FILE_NAME, "r")
csvoutFile = open(FILEOUTPATH, "w", newline='')

reader = csv.reader(csvFile)
writer = csv.writer(csvoutFile)

print("文件读取完毕")

graph = nx.DiGraph()

print("开始构建有向图")
for item in reader:
    graph.add_edge(item[0], item[1])

node_list = graph.nodes

print("开始计算pagerank")
result = nx.pagerank(graph)
print("pagerank计算结果: ", result)

print("开始讲计算结果存入csv")
for node_id in node_list:
    # pg_dict = {"id": node_id, "pagerank": result[node_id]}
    print(node_id, result[node_id])
    writer.writerow([node_id, result[node_id]])
