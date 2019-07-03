import csv
import numpy as  np
from tqdm import tqdm
from multiprocessing.dummy import Pool


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
    FILE_PATH = "E:/IWork/GPU-accelerate/builds/linux/gephiResult_csv/"
    FILE_GRAPH_PATH = "../resultDataset/" + GRAPH_FILE_NAME + _CSV

    layoutFile = open(FILE_PATH + LAYOUT_FILE_NAME + _CSV, "r")
    graphFile = open(FILE_GRAPH_PATH, "r")
    recordFile = open('../layout_position/experiment_gephi_save.txt', 'a')

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

    # print(posList)

    # 读取边数据
    print('读取边数据')
    for link in graphFileReader:
        links.append({'source': link[0], 'target': link[1]})

    # print(links)

    posListLength = len(posList)
    linksLength = len(links)
    posListLength2 = np.square(posListLength)
    countNum = 0  # 当前迭代次数,用来统计百分比
    # print(posListLength)
    # 开始计算节点之间的总距离
    print("开始计算节点之间的总距离")
    pbar = tqdm(total=posListLength2)
    for node in posList:
        for item in posList:
            # if node['id'] != item['id']:  # 这里其实根本没必要判断，反正是0，并且判断会影响性能。
            sumNodeDistance += calEuclideanDistance(node['position'], item['position'])
            pbar.update(1)
            # print('Total sumNodeDistance percent: {:.2%}'.format(float(countNum) / float(posListLength2)))
            # countNum += 1
            # print("sumNodeDistance is ", sumNodeDistance)

    pbar.close()
    countNum = 0

    # 开始计算节点之间的总距离
    print("开始计算边之间的总距离")
    for link in tqdm(links):
        sourcePos = posList[next(index for (index, d) in enumerate(posList) if d["id"] == link['source'])]['position']
        targetPos = posList[next(index for (index, d) in enumerate(posList) if d["id"] == link['target'])]['position']
        sumLinkDistance += calEuclideanDistance(sourcePos, targetPos)
        # print('Total sumLinkDistance percent: {:.2%}'.format(float(countNum) / float(linksLength)))
        countNum += 1
        # print("sumLinkDistance is ", sumLinkDistance)

    # 计算布局质量
    q = 1 / ((sumLinkDistance / linksLength) / (sumNodeDistance / posListLength2))
    # q = (sumLinkDistance / linksLength) / (sumNodeDistance / posListLength2)
    txt = LAYOUT_FILE_NAME + "布局质量为：" + str(q)
    recordFile.write('\n')
    recordFile.write(txt)
    recordFile.write('\n')
    print(txt)
    # print(LAYOUT_FILE_NAME + "布局质量为：", q)


# arguments = [
#     ['3elt/FruchtermanReingoldLayout', '3elt'],
#     ['3elt/OpenOrdLayout', '3elt'],
#     ['3elt/YifanHuLayout', '3elt'],
#
#     # ['1138_bus/YifanHuLayout', '1138_bus'],
#     # ['1138_bus/YifanHuLayout', '1138_bus'],
#     # ['1138_bus/YifanHuLayout', '1138_bus'],
#
#     ['commanche_dual/FruchtermanReingoldLayout', 'commanche_dual'],
#     ['commanche_dual/OpenOrdLayout', 'commanche_dual'],
#     ['commanche_dual/YifanHuLayout', 'commanche_dual'],
#
#     ['facebook_combined2/FruchtermanReingoldLayout', 'facebook_combined2'],
#     ['facebook_combined2/OpenOrdLayout', 'facebook_combined2'],
#     ['facebook_combined2/YifanHuLayout', 'facebook_combined2'],
#
#     ['fe_4elt2/FruchtermanReingoldLayout', 'fe_4elt2'],
#     ['fe_4elt2/OpenOrdLayout', 'fe_4elt2'],
#     ['fe_4elt2/YifanHuLayout', 'fe_4elt2'],
#
#     ['twitter_combined/OpenOrdLayout', 'twitter_combined'],
#     ['twitter_combined/YifanHuLayout', 'twitter_combined'],
#
# ]

def multi_wrapper(args):
    return quality(*args)


arguments1 = ['3elt/FruchtermanReingoldLayout', '3elt/OpenOrdLayout', '3elt/YifanHuLayout',
              'commanche_dual/FruchtermanReingoldLayout', 'commanche_dual/OpenOrdLayout'
                                                          'commanche_dual/YifanHuLayout',
              'facebook_combined2/FruchtermanReingoldLayout',
              'facebook_combined2/OpenOrdLayout',
              'facebook_combined2/YifanHuLayout', 'fe_4elt2/FruchtermanReingoldLayout', 'fe_4elt2/OpenOrdLayout',
              'fe_4elt2/YifanHuLayout', 'twitter_combined/OpenOrdLayout',
              'twitter_combined/YifanHuLayout',
              ]
arguments2 = ['3elt', '3elt', '3elt', 'commanche_dual', 'commanche_dual', 'commanche_dual', 'facebook_combined2',
              'facebook_combined2', 'facebook_combined2', 'fe_4elt2', 'fe_4elt2', 'fe_4elt2', 'twitter_combined',
              'twitter_combined']

# for arr in arguments:
#     print(arr[1] + " 数据正在被计算")
#     quality(arr[0], arr[1])

# Make the Pool of workers
#
# zip_args = list(zip(arguments1, arguments2))
# pool = Pool()
#
# # Open the urls in their own threads
# # and return the results
# pool.map(multi_wrapper, zip_args)
#
# # results = pool.map(quality,
# #                    arguments1, arguments2)
# # close the pool and wait for the work to finish
# pool.close()
# pool.join()

quality('1138_bus/FruchtermanReingoldLayout', '1138_bus')
quality('1138_bus/OpenOrdLayout', '1138_bus')
