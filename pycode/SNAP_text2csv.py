import csv

# 文件名
# FILENAME = 'twitter_combined.csv'


def test2csv(FILENAME):

    # 读取文件的文件夹路径
    FILEINNAME = '../dataset/'
    # 结果文件的文件夹路径
    FILEOUTNAME = '../resultDataset/'

    # 读取文件的路径
    FILEINPATH = FILEINNAME + FILENAME
    # 结果文件的路径
    FILEOUTPATH = FILEOUTNAME + FILENAME

    csvFile = open(FILEINPATH, "r")
    csvoutFile = open(FILEOUTPATH, "w", newline='')

    reader = csv.reader(csvFile)
    writer = csv.writer(csvoutFile)

    list = []
    # 读文件并且处理
    for item in reader:
        result = item[0].split(' ')
        # print(result)
        list_item = {'source': result[0], 'target': result[1]}
        print(list_item)
        list.append(list_item)

    csvFile.close()

    # 讲处理后的文件写入csv中
    # head_info = ['source', 'target']
    # writer.writerow(head_info)

    for item in list:
        w_row = [item['source'], item['target']]
        writer.writerow(w_row)

    csvoutFile.close()
    return "finsh test2csv "
