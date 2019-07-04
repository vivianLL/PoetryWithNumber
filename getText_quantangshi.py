# -*- coding:utf-8*-
import os
import os.path
import re
import time
time1=time.time()

# 合并同一个文件夹下多个txt
def MergeTxt(filepath,outfile):
    poemset = set()
    for parent, dirnames, filenames in os.walk(filepath):
        for filepath in filenames:
            txtPath = os.path.join(parent, filepath)
            f = open(txtPath)
            line = f.read()
            line = line.replace('。。', '。')      # 将两个句号替换为一个句号
            line = line.replace('！', '。')        # 将感叹号替换为句号
            line = '。'.join(line.split('。')[:-1])+'。'   # 令句子以最后一个句号结尾
            poem = re.sub("（.*?）", "", line)     # 去除括号里的内容
            poem = re.sub("。卷.*", "。", poem)    # 去除“卷六百五十四”这种
            poemset.add(poem)
    print(len(poemset))

    k = open(outfile, 'w', encoding='utf-8')
    for poem in poemset:
        if poem!='':
            k.write(poem+"\n")
    k.close()
    print("merge finished!")

# 提取出带数字的诗
def extractNumberPoemtry(inputfile,outfile):
    with open(inputfile,'r',encoding="utf-8") as f1, open(outfile,'w') as f2:
        for line in f1:
            if '_' in line:
                continue
            if re.match(".*[一二三四五六七八九十百千万亿].*",line):
                f2.write(line)



if __name__ == '__main__':
  MergeTxt("D:/Data/poetry/quantangshi/quantangshi/","D:/Data/poetry/quantangshi/quantangshi_all.txt")
  extractNumberPoemtry("D:/Data/poetry/quantangshi/quantangshi_all.txt", "D:/Data/poetry/quantangshi/quantangshi_number.txt")
  time2 = time.time()
  print('总共耗时：' + str(time2 - time1) + 's')
