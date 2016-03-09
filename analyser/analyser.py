from __future__ import division
from bs4 import BeautifulSoup
import os

def get_file_list(dir_path):
    return os.listdir(dir_path)

def get_text_len(soup):
    return len("".join(soup.get_text().split()))

def get_heimu_len(soup):
    heimus = soup.find_all('span', class_="heimu")
    heimus_len = sum([len([heimu.string for heimu in heimus])])
    return heimus_len

def out_put(result, name):
    file = open(name, "w")
    for i in result:
        file.write(i[1]+"\t"+str(i[0])+"\t"+urls[i[1]]+"\n")
    file.close()

heimu_len = {}
text_len = {}
urls = {}

file_list = get_file_list("../datas")
count = 0
file_num = len(file_list)
for file_name in file_list:
    count += 1
    print("[INFO]processing:%s(%d/%d)"%(file_name, count, file_num))
    file = open("./cleaned_datas/"+file_name ,"r")
    file.readline()
    urls[file_name] = file.readline()
    file.readline()
    content = file.read()
    soup = BeautifulSoup(content, "html.parser", from_encoding='utf-8')
    heimu_len[file_name] = get_heimu_len(soup)
    text_len[file_name] = get_text_len(soup)
    file.close()
heimu_ratio = [(heimu_len[i]/text_len[i], i) for i in heimu_len]
result = sorted(heimu_ratio, reverse=True)
result2 = sorted([(heimu_len[i], i) for i in heimu_len], reverse=True)
print("Done! :) "+str(result)+"\n"+str(result2))
out_put(result, "result")
out_put(result2, "result2")
