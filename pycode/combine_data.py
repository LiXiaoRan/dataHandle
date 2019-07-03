import csv
from multiprocessing.dummy import Pool as ThreadPool

_CSV = ".csv"


def merge_data(FILE_NAME):
    FILE_PATH = "../resultDataset/"
    FILE_CC_PATH = "../igraph_result/"
    FILE_OUT_PATH = FILE_PATH + FILE_NAME + "_pg_cc" + _CSV

    print("读取文件")
    csvFilepg = open(FILE_PATH + FILE_NAME + "_pg" + _CSV, "r")
    csvFilecc = open(FILE_CC_PATH + FILE_NAME + "_cc" + _CSV, "r")
    csvoutFile = open(FILE_OUT_PATH, "w", newline='')

    reader_pg = csv.reader(csvFilepg)
    reader_cc = csv.reader(csvFilecc)
    writer = csv.writer(csvoutFile)

    print("读取文件完毕")
    nodeid_list = []
    pgrank_list = []
    cc_list = []

    print("装载 " + FILE_PATH + FILE_NAME + "_pg" + _CSV + " 的数据")
    for item in reader_pg:
        nodeid_list.append(item[0])
        pgrank_list.append(item[1])

    print("装载 " + FILE_PATH + FILE_NAME + "_cc" + _CSV + " 的数据")
    for item in reader_cc:
        cc_list.append(item[1])

    print("开始讲数据写入: " + FILE_OUT_PATH)
    print("数据结构为；nodeid,pagerank,closeness_centrality")
    for nodeid, pgrank, cc in zip(nodeid_list, pgrank_list, cc_list):
        writer.writerow([nodeid, pgrank, cc])

    print("写入完毕")
    csvFilepg.close()
    csvFilecc.close()
    csvoutFile.close()


# merge_data("Slashdot0902")
# merge_data("Slashdot0902")

# Make the Pool of workers
pool = ThreadPool(8)
# Open the urls in their own threads
# and return the results
results = pool.map(merge_data,
                   ["3elt", "bcsstk31"])
# close the pool and wait for the work to finish
pool.close()
pool.join()
