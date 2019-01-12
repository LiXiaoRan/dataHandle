import SNAP_text2csv
import pageRankCompute
MAIN_FILE_NAME = "Cit_HepTh"

# 开始自动转csv
print(SNAP_text2csv.test2csv(MAIN_FILE_NAME+'.csv'))

# 自动计算pagerank
print(pageRankCompute.compute_pg(MAIN_FILE_NAME))
