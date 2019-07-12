# coding=utf-8
import csv
from tqdm import tqdm

from igraph import *
import json


# 计算布局数据
def cal_back_layout_data(result, layout_type):
    nodes = []
    links = []

    for node in tqdm(result['nodes']):
        nodes.append(node['id'])
    for link in tqdm(result['links']):
        source = nodes.index(link['source'])
        target = nodes.index(link['target'])
        links.append((source, target))

    # 设置图为有向图 环状RT树布局和层次化布局不支持有向图
    if layout_type == "rt_circular" or layout_type == "sugiyama":
        graph = Graph()
    else:
        graph = Graph(directed=True)

    graph.add_vertices(len(nodes))
    graph.add_edges(links)
    lay = graph.layout(layout_type)
    in_degree_list = []
    out_degree_list = []
    if layout_type != "rt_circular" and layout_type != "sugiyama":
        in_degree_list = graph.vs.indegree()
        out_degree_list = graph.vs.outdegree()
    degree_list = graph.vs.degree()

    for i, row in enumerate(lay):
        result['nodes'][i]['x'] = row[0]
        result['nodes'][i]['y'] = row[1]
        result['nodes'][i]['degree'] = degree_list[i]
        if layout_type != "rt_circular" and layout_type != "sugiyama":
            result['nodes'][i]['in'] = in_degree_list[i]
            result['nodes'][i]['out'] = out_degree_list[i]

    for link in result['links']:
        for node in result['nodes']:
            if link['source'] == node['id']:
                link['x1'] = node['x']
                link['y1'] = node['y']
            if link['target'] == node['id']:
                link['x2'] = node['x']
                link['y2'] = node['y']

    return result


dataNmae = "twitter_combined"


def computeLayout(FileName, type):
    _CSV = ".csv"
    FILE_PATH = "../resultDataset/"
    FILE_OUT_PATH = "../JsonData/gephi/" + FileName + "/" + type + ".json"

    csvFile = open(FILE_PATH + FileName + _CSV, "r")
    jsonFile = open(FILE_OUT_PATH, "w")

    reader = csv.reader(csvFile)

    temp_nodes = []
    nodes = []
    links = []

    for item in tqdm(reader):
        if temp_nodes.count(item[0]) == 0:
            temp_nodes.append(item[0])
        if temp_nodes.count(item[1]) == 0:
            temp_nodes.append(item[1])

        links.append({'source': item[0], 'target': item[1]})

    for item in temp_nodes:
        nodes.append({'id': item})

    result = {'nodes': nodes, 'links': links}

    print("开始计算布局: " + FileName)
    layout_result = cal_back_layout_data(result, 'fr')

    json_data = json.dumps(layout_result)
    # print(json_data)

    print("存入json: " + FileName)
    jsonFile.write(json_data)
    jsonFile.close()


# computeLayout("twitter_combined", "fr")
computeLayout("web_Google", "fr")
computeLayout("web_Stanford", "fr")

