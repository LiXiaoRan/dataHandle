import SNAP_text2csv
import mtx2csv
import pageRankCompute
MAIN_FILE_NAME = "3elt"

# 开始自动转csv
# print(SNAP_text2csv.test2csv(MAIN_FILE_NAME+'.csv'))

# mtx2csv
print(mtx2csv.trans(MAIN_FILE_NAME))

# 自动计算pagerank
print(pageRankCompute.compute_pg(MAIN_FILE_NAME))
