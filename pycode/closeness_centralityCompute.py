import csv
import networkx as nx


def closeness_centrality_compute(FILE_NAME):
    _CSV = ".csv"
    FILE_PATH = "../resultDataset/"
    FILE_OUT_PATH = FILE_PATH + FILE_NAME + "_cc" + _CSV

    graph = nx.DiGraph()

    csvFile = open(FILE_PATH + FILE_NAME + _CSV, "r")
    csvoutFile = open(FILE_OUT_PATH, "w", newline='')

    reader = csv.reader(csvFile)
    writer = csv.writer(csvoutFile)

    print("文件读取完毕")

    graph = nx.DiGraph()

    print("开始构建有向图")
    for item in reader:
        graph.add_edge(item[0], item[1])

    node_list = graph.nodes

    print("closeness_centrality")
    result = nx.closeness_centrality(graph, wf_improved=True)
    print("closeness_centrality计算结果: ", result)

    print("开始讲计算结果存入csv")
    for node_id in node_list:
        print(node_id, result[node_id])
        writer.writerow([node_id, result[node_id]])

    csvFile.close()
    csvoutFile.close()
    return "closeness_centrality compute finsh "


closeness_centrality_compute("Cit_HepPh")
