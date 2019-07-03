import csv
import json
import csv2json

_CSV = ".csv"
_JSON = ".json"


def transfer(csvEdgeFileName, csvPosFileName):
    EDGE_FILE_PATH = "../resultDataset/"
    POS_FILE_PATH = "../layout_position/"
    JSON_FILE_OUT_PATH = "../JsonData/" + csvPosFileName + _JSON
    FILE_OUT_PATH = POS_FILE_PATH + csvPosFileName + _JSON

    print("读取文件: " + csvEdgeFileName)

    graphFile = open(EDGE_FILE_PATH + csvEdgeFileName + _CSV, "r")
    layoutFile = open(POS_FILE_PATH + csvPosFileName + _CSV, "r")
    jsonFile = open(JSON_FILE_OUT_PATH, "w")

    reader_edge = csv.reader(graphFile)
    reader_pos = csv.reader(layoutFile)

    edgeList = []
    posList = []

    print("节点数据处理: " + csvEdgeFileName)

    for pos in reader_pos:
        # 讲每个节点的id作为key，x和y作为value存入dict
        # print(pos)
        posList.append({'x': pos[1], 'y': pos[2]})

    print("边数据处理: " + csvEdgeFileName)

    for link in reader_edge:
        edgeList.append({'source': link[0], 'target': link[1]})

    data = {'nodes': posList, 'links': edgeList}

    json_data = json.dumps(data)
    # print(json_data)

    print("存入json: " + csvEdgeFileName)
    jsonFile.write(json_data)
    jsonFile.close()

    print(csvEdgeFileName + " 操作 完毕 ！ ")


# transfer('3elt', '3elt.csv_500')

transferFileList = [['3elt', '3elt.csv_500', ], ['1138_bus', '1138_bus.csv_5000'],
                    ['commanche_dual', 'commanche_dual.csv_5000'],
                    ['facebook_combined2', 'facebook_combined2.csv_5000'], ['fe_4elt2', 'fe_4elt2.csv_5000'],
                    ['twitter_combined', 'twitter_combined.csv_5000']]

for fun in transferFileList:
    transfer(fun[0], fun[1])
