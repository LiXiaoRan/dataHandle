import csv
import json


def read_csv(file):
    csv_rows = []
    item = {}
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            # csv_rows.extend([{title[i]: row[title[i]] for i in range(len(title))}])
            item = {title[0]: row[title[0]], title[1]: int(row[title[1]]), title[2]: float(row[title[2]])}
            csv_rows.append(item)
        return csv_rows


def write_json(data, json_file, format=None):
    with open(json_file, "w") as f:
        if format == "good":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),
                               ensure_ascii=False))
        else:
            f.write(json.dumps(data))


# print(read_csv('../dataset/vega-liteData.csv'))

write_json(read_csv('../dataset/vega-liteData.csv'), '../resultDataset/vega-liteData.json', 'good')
