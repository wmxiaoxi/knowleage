#coding:utf-8
import xlrd
# ##读取
# data=xlrd.open_workbook(r'C:\Users\wmxia\Desktop\项目\ip价值评估\IP价值评估用例-20200310.xls')
# # table=data.sheets()[0]   #通过索引顺序获取
# # table=data.sheet_by_index(0)#通过索引顺序获取
# table=data.sheet_by_name(u'模板导入')#通过名称获取
# nrows=table.nrows  #获取总行数
# ncols=table.ncols  #获取总列数
#
#
# print(table.row_values(0))#获取第一行的值
# print(table.col_values(3))#获取第4列的值
#



#
# #读取封装
#
# data = xlrd.open_workbook(r'C:\Users\wmxia\Desktop\11.xls')
# table = data.sheet_by_name('Sheet1')
# # 获取第一行作为key值
# keys = table.row_values(0)
# # 获取总行数
# rowNum = table.nrows
# print(rowNum)
# colNum = table.ncols
# list=[]
# dict={}
# for i in range(1,rowNum):
#     a=table.row_values(i)
#     list.append(dict)
#     for j in range(0,colNum):
#         dict[keys[j]]=a[j]
#
# print(list)


import time
print(time.strftime('%Y-%m-%d %H%M%S',time.localtime()))
