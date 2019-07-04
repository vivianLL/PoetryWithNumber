import json
import os
import re
from langconv import *
import time
time1=time.time()

# 合并同一个文件夹下多个txt
def MergeTxt(filepath,outfile):
    poemset = set()
    for parent, dirnames, filenames in os.walk(filepath):
        for filepath in filenames:
            txtPath = os.path.join(parent, filepath)
            with open(txtPath, encoding='utf-8') as f:
                s = json.load(f)
                for item in s:
                    sentence = ''.join(item["paragraphs"])
                    sentence = Converter('zh-hans').convert(sentence)   # 繁体转简体
                    poem = re.sub("{.*?}", "", sentence)                # 去除{}里的内容
                    poem = re.sub("（.*?）", "", poem)                  # 去除（）里的内容
                    poem = re.sub("-.*?。", "", poem)                   # 去除“-143-。”这种内容
                    poem.replace("。。", "。")                           # 将两个句号替换为一个句号
                    poemset.add(poem)
    print(len(poemset))

    k = open(outfile, 'w', encoding='utf-8')
    for poem in poemset:
        if poem != '':
            k.write(poem + "\n")
    k.close()
    print("merge finished!")

# 提取出带数字的诗
def extractNumberPoemtry(inputfile,outfile):
    with open(inputfile,'r',encoding="utf-8") as f1, open(outfile,'w',encoding="utf-8") as f2:
        for line in f1:
            if '□' in line:
                continue
            if re.match(".*[一二三四五六七八九十百千万亿].*",line):
                f2.write(line.replace('。。', '。').replace('！。', '。').replace('！', '。').replace('Y', '').replace('。”。', '。').replace('：“','，').replace('”','').replace('“','，'))

# 把几个数据集的文本合起来
def mergefile(inputfile1,inputfile2,outfile):
    poemset = set()
    with open(inputfile1, 'r', encoding="utf-8") as f1, open(inputfile2, 'r', encoding="utf-8") as f2, open(outfile, 'w', encoding="utf-8") as f3:
        for line1 in f1:
            poemset.add(line1)
        for line2 in f2:
            poemset.add(line2)
        for line in poemset:
            f3.write(line)


if __name__ == '__main__':
    # MergeTxt("D:/Data/poetry/chinesepoetry/chinesepoetry/","D:/Data/poetry/chinesepoetry/chinesepoetry_all.txt")
    # extractNumberPoemtry("D:/Data/poetry/chinesepoetry/chinesepoetry_all.txt","D:/Data/poetry/chinesepoetry/chinesepoetry_number.txt")
    mergefile("D:/Data/poetry/chinesepoetry/chinesepoetry_number.txt", "D:/Data/poetry/quantangshi/quantangshi_number.txt", "D:/Data/poetry/poetry_with_number.txt")
    time2 = time.time()
    print('总共耗时：' + str(time2 - time1) + 's')
