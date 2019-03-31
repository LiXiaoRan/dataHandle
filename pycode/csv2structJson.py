import csv
import csv2json

_CSV = ".csv"
_JSON = ".json"


def transfer(csvEdgeFileName, csvPosFileName):
    EDGE_FILE_PATH = "../resultDataset/"
    POS_FILE_PATH = "../PosData/"
    FILE_OUT_PATH = POS_FILE_PATH + csvPosFileName + _JSON

    print("读取文件")

    reader_edge = csv.reader(EDGE_FILE_PATH + csvEdgeFileName + _CSV)
    reader_pos = csv.reader(POS_FILE_PATH + csvPosFileName + _CSV)

    edgeList = []
    posList = {}

    for pos in reader_pos:
        # 讲每个节点的id作为key，x和y作为value存入dict
        posList[str(pos[0])] = {'x': pos[1], 'y': pos[2]}

    