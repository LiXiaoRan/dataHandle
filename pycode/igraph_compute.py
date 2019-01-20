import igraph
import csv


def compute_cc(FILE_NAME):
    _CSV = ".csv"
    FILE_PATH = "../igraph_result/"
    FILE_OUT_PATH = FILE_PATH + FILE_NAME + "_cc" + _CSV

    csvFile = open(FILE_PATH + FILE_NAME + _CSV, "r")
    csvoutFile = open(FILE_OUT_PATH, "w", newline='')

    reader = csv.reader(csvFile)
    writer = csv.writer(csvoutFile)

    print(FILE_NAME, " 文件读取完毕")

    graph = igraph.Graph(directed=True)

    nodes = []
    links = []

    print(FILE_NAME, " 开始构建有向图")
    for item in reader:
        graph.add_edge(item[0], item[1])

    pass
