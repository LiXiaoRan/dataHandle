#!/usr/bin/python
# -*- coding:utf-8 -*-
import snap
import pandas as pd
import numpy as np
import csv


def snap_cc_compute(FILE_NAME):
    _CSV = ".csv"

    FILE_PATH = "../resultDataset/"
    FILE_OUT_PATH = "../igraph_result/" + FILE_NAME + "_cc" + _CSV

    data = pd.read_csv(FILE_PATH + FILE_NAME + _CSV, header=None)
    csvoutFile = open(FILE_OUT_PATH, "w")
    writer = csv.writer(csvoutFile,lineterminator='\n')

    data0 = np.unique(data.iloc[:, 0].append(data.iloc[:, 1]))
    print("read  %s,  file complete，totol  %d  nodes  %d edges " % (FILE_NAME, len(data0), len(data)))
    # print("node list  is  " + data0)
    G2 = snap.TNGraph.New()
    count=0;
    countNum = len(data0)
    print(" start build nodes")
    nodes = data0.tolist()
    # for node in nodes:
    #     # print type (node)
    #     G2.AddNode(nodes.index(node))
    #     count=count+1

    while count != countNum:
        G2.AddNode(count)
        count=count+1

    count=0
    edgeNum=len(data)
    print(" start add edges")
    for row in data.itertuples(index=False):
        G2.AddEdge(nodes.index(row[0]),nodes.index(row[1]))
        print('add edges percent: {:.2%}'.format(float(count) / float(edgeNum)))
        count+=1

    print(" start compute cc ")

    count = 0
    for NI in G2.Nodes():
        count = count + 1
        CloseCentr = snap.GetClosenessCentr(G2, NI.GetId())
        print('compute percent: {:.2%}'.format(float(count) / float(countNum)))
        writer.writerow([nodes[NI.GetId()], CloseCentr])
        # print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)

    csvoutFile.close()
    print("succesfull")


snap_cc_compute("Delor338K")
