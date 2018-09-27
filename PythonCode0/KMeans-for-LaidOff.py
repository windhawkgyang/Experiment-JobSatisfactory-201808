# coding:utf-8
# 本程序进行一个初步实验：
# 如果直接使用CERT5.2中的用户LDAP中关联的Leave与Laid off数量关系，采用KMeans能否发现规律？
# 或者先做一个自动PCA，然后再使用KMeans能否发现规律？

# 为了作图的方便，需要重新确定分析的1999个用户中，场景二的30个Insiders的坐标序号

import os, sys
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np

print '......<<<<<<', '本程序将试着用Kmeans与PCA作为工具初步分析Leave/LaidOff Relationships>>>>>>......'
print '首先读入待分析的文件数据，以及CERT5.2中Insiders_2列表...\n'
f_1 = open('CERT5.2-Leave-Relationship_Counts.csv', 'r')
f_2 = open('CERT5.2-LaidOff-Relationship_Counts.csv', 'r')
f_1_lst = f_1.readlines()
f_2_lst = f_2.readlines()
f_1.close()
f_2.close()

InsiderDir_2 = os.path.dirname(sys.path[0]) + '\\' + 'r5.2-2'
Insiders_2 = []
for user in os.listdir(InsiderDir_2):
    Insiders_2.append(user[7:-4])
print 'Insiders 2提取完毕...\t', len(Insiders_2), Insiders_2[:5], '\n'
Insiders_2.sort()

Users_CERT52 = []
# CERT5.2 Laid Off Company Relationships Counts for all Users
# MMK1532,No,0,10,17,68,91
# NTB0710,No,2,14,24,53,91
# MTD0971,2010-10,2,3,10,34,54
for line in f_1_lst:
    line_lst = line.strip('\n').strip(',').split(',')
    if len(line_lst) < 2:
        continue
    Users_CERT52.append(line_lst[0])
print 'CERT5.2 用户提取完毕...\t', len(Users_CERT52), Users_CERT52[:5], '\n'


print '提取对应用户的坐标位置...\n'
Insiders_2_Index = []
for user in Users_CERT52:
    if user in Insiders_2:
        Insiders_2_Index.append(Users_CERT52.index(user))
        #print user, Users_CERT52.index(user), '\n'
print 'Insiders_2的坐标提取完毕...\t', len(Insiders_2_Index), Insiders_2_Index[:5], '\n'
print '......<<<<<<准备工作完毕，开始进行实验>>>>>>......\n\n'



print '......<<<<<<首先直接使用KMeans聚类，然后绘图分析>>>>>>......\n\n'
print '添加控制开关...\n'
Flag = 1
if Flag > 0:
    # 开关开启时进行实验
    print 'Step-1. 提取目标数组...\n'
    Leave_Counts = []
    LaidOff_Counts = []
    for line in f_1_lst:
        line_lst = line.strip('\n').strip(',').split(',')
        if len(line_lst) < 2:
            continue
        # VCM0992,No,1,13,22,82,120
        counts = []
        counts.append(float(line_lst[2]))
        counts.append(float(line_lst[3]))
        counts.append(float(line_lst[4]))
        counts.append(float(line_lst[5]))
        counts.append(float(line_lst[6]))
        Leave_Counts.append(counts)
    for i in range(10):
        print Leave_Counts[i], '\n'
    print 'Leave_Counts数组初始化完毕...\n'

    for line in f_2_lst:
        line_lst = line.strip('\n').strip(',').split(',')
        if len(line_lst) < 2:
            continue
        # VCM0992,No,1,13,22,82,120
        counts = []
        counts.append(float(line_lst[2]))
        counts.append(float(line_lst[3]))
        counts.append(float(line_lst[4]))
        counts.append(float(line_lst[5]))
        counts.append(float(line_lst[6]))
        LaidOff_Counts.append(counts)
    for i in range(10):
        print LaidOff_Counts[i], '\n'
    print 'LaidOff_Counts数组初始化完毕...\n'




sys.exit()