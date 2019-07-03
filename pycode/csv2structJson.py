import csv
import json
import os

_CSV = ".csv"
_JSON = ".json"


def transfer(csvEdgeFileName, csvPosFileName, gephi=False):
    EDGE_FILE_PATH = "../resultDataset/"
    POS_FILE_PATH = "../layout_position/"
    POS_FILE_PATH_GEPHI = "E:/IWork/GPU-accelerate/builds/linux/gephiResult_csv/"
    JSON_FILE_OUT_PATH = "../JsonData/" + csvPosFileName + _JSON

    print("读取文件: " + csvEdgeFileName)

    graphFile = open(EDGE_FILE_PATH + csvEdgeFileName + _CSV, "r")

    if gephi:
        layoutFile = open(POS_FILE_PATH_GEPHI + csvPosFileName + _CSV, "r")
        JSON_FILE_OUT_PATH = "../JsonData/gephi/" + csvPosFileName + _JSON


    else:
        layoutFile = open(POS_FILE_PATH + csvPosFileName + _CSV, "r")

    # if not os.path.exists(JSON_FILE_OUT_PATH):
    #     os.mkdir(JSON_FILE_OUT_PATH)

    jsonFile = open(JSON_FILE_OUT_PATH, "w")

    reader_edge = csv.reader(graphFile)
    reader_pos = csv.reader(layoutFile)

    edgeList = []
    posList = []

    print("节点数据处理: " + csvEdgeFileName)

    for pos in reader_pos:
        # 讲每个节点的id作为key，x和y作为value存入dict
        # print(pos)
        posList.append({'x': float(pos[1]), 'y': float(pos[2])})

    print("边数据处理: " + csvEdgeFileName)

    for link in reader_edge:
        edgeList.append({'source': int(link[0]), 'target': int(link[1])})

    data = {'nodes': posList, 'links': edgeList}

    json_data = json.dumps(data)
    # print(json_data)

    print("存入json: " + csvEdgeFileName)
    jsonFile.write(json_data)
    jsonFile.close()

    print(csvPosFileName + " 操作 完毕 ！ ")


# transfer('3elt', '3elt.csv_500')

transferFileList = [['3elt', '3elt.csv_500', ], ['1138_bus', '1138_bus.csv_5000'],
                    ['commanche_dual', 'commanche_dual.csv_5000'],
                    ['facebook_combined2', 'facebook_combined2.csv_5000'], ['fe_4elt2', 'fe_4elt2.csv_5000'],
                    ['twitter_combined', 'twitter_combined.csv_5000']]

# for fun in transferFileList:
#     transfer(fun[0], fun[1])

transferFileList_gephi = [
    ['3elt', '3elt/FruchtermanReingoldLayout'],
    ['3elt', '3elt/OpenOrdLayout'],
    ['3elt', '3elt/YifanHuLayout'],

    ['1138_bus', '1138_bus/FruchtermanReingoldLayout'],
    ['1138_bus', '1138_bus/OpenOrdLayout'],
    ['1138_bus', '1138_bus/YifanHuLayout'],

    ['commanche_dual', 'commanche_dual/FruchtermanReingoldLayout'],
    ['commanche_dual', 'commanche_dual/OpenOrdLayout'],
    ['commanche_dual', 'commanche_dual/YifanHuLayout'],

    ['facebook_combined2', 'facebook_combined2/FruchtermanReingoldLayout'],
    ['facebook_combined2', 'facebook_combined2/OpenOrdLayout', ],
    ['facebook_combined2', 'facebook_combined2/YifanHuLayout', ],

    ['fe_4elt2', 'fe_4elt2/FruchtermanReingoldLayout'],
    ['fe_4elt2', 'fe_4elt2/OpenOrdLayout'],
    ['fe_4elt2', 'fe_4elt2/YifanHuLayout'],

    ['twitter_combined', 'twitter_combined/OpenOrdLayout'],
    ['twitter_combined', 'twitter_combined/YifanHuLayout'],

]

for fun in transferFileList_gephi:
    transfer(fun[0], fun[1], True)
