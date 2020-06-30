import xlrd
import requests
import sqlite3

wb = xlrd.open_workbook("1.xls")#打开文件
sheet1 = wb.sheet_by_index(0)

list_item_data = cols = sheet1.col_values(0)
list_gp_data = sheet1.col_values(1)
list_name_data =  sheet1.col_values(2)

loot_data = []
for i,j,k in zip(list_item_data,list_gp_data,list_name_data):
  if i != "物品":
    url = "https://60.wowfan.net/?search={}&opensearch".format(i)
    response  = requests.get(url).json()
    temp = {'item':response[7][0][1],'name':k,'gp':j}
    loot_data.append(temp)
# 2020-06-17 21:32:32

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
for i in loot_data:
    c.execute('INSERT INTO point_record (item,gp,name,time) VALUES (?,?,?,?) ',(i['item'],i['gp'],i['name'],'2020-06-17 21:32:32'))
#update point_score set gp=0 where gp <0
conn.commit()
conn.close()