import csv

FILENAME = 'gplus_combined.csv'

FILEINNAME = '../dataset/'
FILEOUTNAME = '../resultDataset/'

FILEINPATH = FILEINNAME + FILENAME
FILEOUTPATH = FILEOUTNAME + FILENAME

csvFile = open(FILEINPATH, "r")
csvoutFile = open(FILEOUTPATH, "w")

reader = csv.reader(csvFile)
writer = csv.writer(csvoutFile)

list = []
for item in reader:
    result = item[0].split(' ')
    list_item = {'source': result[0], 'target': result[1]}
    print(list_item)
    list.append(list_item)

csvFile.close()

head_info = ['source', 'target']
writer.writerow(head_info)

for item in list:
    w_row = [item['source'], item['target']]
    writer.writerow(w_row)

csvoutFile.close()
