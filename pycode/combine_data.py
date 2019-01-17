import csv

_CSV = ".csv"


def merge_data(FILE_NAME):
    FILE_PATH = "../resultDataset/"
    FILE_OUT_PATH = FILE_PATH + FILE_NAME + "_pg_cc" + _CSV

    print("读取文件")
    csvFilepg = open(FILE_PATH + FILE_NAME + "_pg" + _CSV, "r")
    csvFilecc = open(FILE_PATH + FILE_NAME + "_cc" + _CSV, "r")
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


    print("开始讲数据写入: "+FILE_OUT_PATH)
    print("数据结构为；nodeid,pagerank,closeness_centrality")
    for nodeid, pgrank, cc in zip(nodeid_list, pgrank_list, cc_list):
        writer.writerow([nodeid, pgrank, cc])

    print("写入完毕")
    csvFilepg.close()
    csvFilecc.close()
    csvoutFile.close()


merge_data("Cit_HepPh")
