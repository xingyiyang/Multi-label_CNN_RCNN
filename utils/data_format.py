# -*- coding:utf-8 -*-
import pandas as pd
import random
import pymysql


def savedata(filename, datalist):
    with open(filename, 'w') as f:
        for data in datalist:
            f.write(str(data)+"\n")
    print("存文件成功")


def readcsv(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        data = pd.read_csv(f)
        data1 = data.id.tolist()
        data2 = data.tag.tolist()
        data3 = data.content_dl.tolist()

    return data1, data2, data3


def readsql():
    print("读数据库")
    # 连接数据库
    db = pymysql.connect("localhost", "root", "123456", "db_multi_tags")
    # 使用cursor()方法创建一个游标对象
    cursor = db.cursor()
    try:
        # 使用execute()方法执行SQL语句
        cursor.execute("SELECT id, key_thirty, tag FROM tb_data where tag not like '%16%';")
        # 使用fetall()获取全部数据
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(e)
    finally:
        # 关闭游标和数据库的连接
        cursor.close()
        db.close()


def makejsondata(data):
    print("处理json数据")
    datalist = []
    for datai in data:
        dictlist = dict()
        dictlist["testid"] = str(datai[0])
        dictlist["features_content"] = datai[1].split("#")
        label_list = datai[2].split(",")
        label_index = []
        for i in label_list:
            label_index.append(int(i)-1)
        dictlist["labels_index"] = label_index
        dictlist["labels_num"] = len(label_list)
        datalist.append(dictlist)
    return datalist


def readfile(filename):
    with open(filename, 'r') as f:
        list = []
        for line in f:
            list.append(line.strip())
    return list


if __name__ == '__main__':
    # data = readsql()
    # datalist = makejsondata(data)
    # savedata("../data/all_data.json", datalist)
    datalist = readfile('../data/all_data.json')
    datalistnew = random.sample(datalist, 2742)
    datalist1 = datalistnew[:1920]
    datalist2 = datalistnew[1920:len(datalistnew)]
    savedata('../data/train.json', datalist1)
    savedata('../data/validation.json', datalist2)


