import csv
import numpy as  np


def calEuclideanDistance(pos1, pos2):
    """计算欧氏距离"""
    vec1 = np.array(pos1)
    vec2 = np.array(pos2)
    # dist = np.sqrt(np.sum(np.square(vec1 - vec2)))
    dist = np.linalg.norm(vec1 - vec2)
    return dist


def quality(LAYOUT_FILE_NAME, GRAPH_FILE_NAME):
    """计算布局质量"""
    _CSV = ".csv"
    FILE_PATH = "../layout_position/"
    FILE_GRAPH_PATH = "../resultDataset/" + GRAPH_FILE_NAME + _CSV

    layoutFile = open(FILE_PATH + LAYOUT_FILE_NAME + _CSV, "r")
    graphFile = open(FILE_GRAPH_PATH, "r")

    layoutFileReader = csv.reader(layoutFile)
    graphFileReader = csv.reader(graphFile)

    posList = []  # 存储id和位置属性
    links = []  # 存储所有边

    sumNodeDistance = 0  # 所有节点的总距离
    sumLinkDistance = 0  # 所有边的总距离

    # 读取布局数据
    print('读取布局数据')
    for position in layoutFileReader:
        # print(position)
        posList.append({'id': position[0], 'position': [float(position[1]), float(position[2])]})

    print(posList)

    # 读取边数据
    print('读取边数据')
    for link in graphFileReader:
        links.append({'source': link[0], 'target': link[1]})

    print(links)

    posListLength = len(posList)
    linksLength = len(links)
    posListLength2=np.square(posListLength)
    countNum = 0  # 当前迭代次数,用来统计百分比
    # print(posListLength)
    # 开始计算节点之间的总距离
    print("开始计算节点之间的总距离")
    for node in posList:
        for item in posList:
            # if node['id'] != item['id']:  # 这里其实根本没必要判断，反正是0，并且判断会影响性能。
            sumNodeDistance += calEuclideanDistance(node['position'], item['position'])
            print('Total sumNodeDistance percent: {:.2%}'.format(float(countNum) / float(posListLength2)))
            countNum += 1
            # print("sumNodeDistance is ", sumNodeDistance)

    countNum = 0

    # 开始计算节点之间的总距离
    print("开始计算边之间的总距离")
    for link in links:
        sourcePos = posList[next(index for (index, d) in enumerate(posList) if d["id"] == link['source'])]['position']
        targetPos = posList[next(index for (index, d) in enumerate(posList) if d["id"] == link['target'])]['position']

        sumLinkDistance += calEuclideanDistance(sourcePos, targetPos)
        print('Total sumLinkDistance percent: {:.2%}'.format(float(countNum) / float(linksLength)))
        countNum += 1
        # print("sumLinkDistance is ", sumLinkDistance)

    # 计算布局质量
    q = (sumLinkDistance / linksLength) / (sumNodeDistance / posListLength2)
    print(LAYOUT_FILE_NAME + "布局质量为：", q)


quality('3elt.csv_5000', '3elt')
