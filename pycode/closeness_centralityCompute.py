import csv
import networkx as nx
from multiprocessing.dummy import Pool as ThreadPool


def closeness_centrality_compute(FILE_NAME):
    _CSV = ".csv"
    FILE_PATH = "../resultDataset/"
    FILE_OUT_PATH = FILE_PATH + FILE_NAME + "_cc" + _CSV

    graph = nx.DiGraph()

    csvFile = open(FILE_PATH + FILE_NAME + _CSV, "r")
    csvoutFile = open(FILE_OUT_PATH, "w", newline='')

    reader = csv.reader(csvFile)
    writer = csv.writer(csvoutFile)

    print(FILE_NAME, " 文件读取完毕")

    graph = nx.DiGraph()

    print(FILE_NAME," 开始构建有向图")
    for item in reader:
        graph.add_edge(item[0], item[1])

    node_list = graph.nodes

    print("开始计算 closeness_centrality ",FILE_NAME)
    result = nx.closeness_centrality(graph, wf_improved=True)
    print(FILE_NAME," closeness_centrality计算结果: ", result)

    print("开始讲计算结果存入csv ",FILE_NAME)
    for node_id in node_list:
        # print(node_id, result[node_id])
        writer.writerow([node_id, result[node_id]])

    csvFile.close()
    csvoutFile.close()
    print("closeness_centrality compute finshed ",FILE_NAME)
    return "closeness_centrality compute finshed "


# closeness_centrality_compute("Email_EuAll")
# closeness_centrality_compute("gplus_combined")
# closeness_centrality_compute("Slashdot0902")
# closeness_centrality_compute("twitter_combined")
# closeness_centrality_compute("web_Google")
# closeness_centrality_compute("web_NotreDame")
# closeness_centrality_compute("web_Stanford")

# Make the Pool of workers
pool = ThreadPool(7)
# Open the urls in their own threads
# and return the results
results = pool.map(closeness_centrality_compute,
                   ["Email_EuAll", "gplus_combined", "Slashdot0902", "twitter_combined", "web_Google", "web_NotreDame",
                    "web_Stanford"])
# close the pool and wait for the work to finish
pool.close()
pool.join()
