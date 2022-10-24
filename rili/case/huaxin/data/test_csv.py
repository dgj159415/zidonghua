import csv
from itertools import islice



def data_csv(filename):
    with open(filename, 'r', encoding="UTF-8") as file:
        # csv.reader(iterable)，iterable 可以为文件或列表对象，读取csv文件中所有的行
        raw = csv.reader(file)
        data = []
        # 对所有行进行遍历
        for line in islice(raw,1,None):
            data.append(line)
    return data
