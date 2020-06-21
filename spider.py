# -*- coding: utf-8 -*-
from requests_html import HTMLSession
import xlsxwriter
import json
from retrying import retry
import time
import re
import sqlite3

@retry(wait_random_min=1000,wait_random_max=5000)
def get_html(url):
  'url'
  session = HTMLSession(
    browser_args=[
				'--no-sand',
				'--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"'
			]
    )#设置浏览器user-agent
  response = session.get(url)
  #response.html.render(timeout=30)
  return response
  
if __name__ == "__main__":
  fightID = input("输入WCL识别符：")
  boss_id_url = "https://cn.classic.warcraftlogs.com/reports/fights-and-participants/"+ fightID +"/0"
  timeURl = "https://cn.classic.warcraftlogs.com/reports/"+ fightID
  #获取time
  timer = get_html(timeURl)
  timeaaa = timer.html.xpath("//script")
  for i in timeaaa:
      a = re.search( r'start_time = \d+', i.text, re.M|re.I)
      if a:
          fighttime=re.search(r'\d+',a.group(0)).group(0)    

  '获取详细boss战ID 请求URL 返回json'
  r = get_html(boss_id_url)
  fightData = json.loads(r.text)
  fight_data = []
  for i in fightData['fights']:
    if 'kill' in i and i['boss'] != '0' and i['kill']:
      #生产详细战斗boss及战斗id列表
      temp = {'name':str(i['name']),'fightID':str(i['id']),"time":str(i['end_time'])}
      fight_data.append(temp)
  

  epgp = [
    {'name':'鲁西弗隆','point':40},{'name':'玛格曼达','point':40},{'name':'基赫纳斯','point':40},{'name':'迦顿男爵','point':40},{'name':'沙斯拉尔','point':40},{'name':'加尔','point':40},{'name':'萨弗隆先驱者','point':40},{'name':'焚化者古雷曼格','point':40},{'name':'管理者埃克索图斯','point':40},{'name':'熔岩爆发','point':60}
  ]
  dkp = [
    {'name':'鲁西弗隆','point':2},{'name':'玛格曼达','point':2},{'name':'基赫纳斯','point':2},{'name':'迦顿男爵','point':2},{'name':'沙斯拉尔','point':2},{'name':'加尔','point':2},{'name':'萨弗隆先驱者','point':2},{'name':'焚化者古雷曼格','point':2},{'name':'管理者埃克索图斯','point':2},{'name':'熔岩爆发','point':4},{'name':'狂野的拉佐格尔','point':3},{'name':'堕落的瓦拉斯塔兹','point':3},{'name':'勒什雷尔','point':3},{'name':'费尔默','point':3},{'name':'埃博诺克','point':3},{'name':'弗莱格尔','point':3},{'name':'克洛玛古斯','point':3},{'name':'奈法利安','point':6}
  ]
  #遍历boss ID列表匹配friendlies列表
  reslot = []
  job_dic= {}
  for i in fight_data:
    temp_name = ""
    for j in fightData['friendlies']:
      if '.'+i['fightID']+'.' in j['fights']:
        temp_name = temp_name + j['name']+","
        job_dic[j['name']] = j['type']
        job_dic.update(job_dic)
    epgpScore = 0
    dkpScore = 0
    for k in epgp:
      if i['name'] == k['name']:
        epgpScore = k['point']
    for l in dkp:
      if i['name'] == l['name']:
        dkpScore = l['point']
    temp = {'boss':i['name'],'name':temp_name,'epgp':epgpScore,'dkp':dkpScore,'time':i['time']}
    reslot.append(temp)

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
for i in reslot:
  a = time.localtime((int(fighttime)+int(i['time']))/1000.0)
  timenow = time.strftime("%Y-%m-%d %H:%M:%S", a)
  c.execute("INSERT INTO point_record (time,dkp,ep,name,boss) VALUES (?,?,?,?,?)",(str(timenow),str(i['dkp']),str(i['epgp']),i['name'],i['boss']))
  #record表更新
  nameall = i['name'].split(',')
  for j in nameall:
    if j :
      c.execute("SELECT * from point_score WHERE name=?",[j])
      recode_res = c.fetchone()
      if recode_res:
        c.execute('UPDATE point_score SET ep=? WHERE name=? ',((recode_res[4]+int(i['epgp'])),recode_res[1]))
      else:
        #print(j)
        a = job_dic[j].upper()
        #print(a)
        c.execute('INSERT INTO point_score (dkp,ep,name,job,gp) VALUES (?,?,?,?,?) ',((int(i['dkp'])),(int(i['epgp'])),j,a,0))
      
conn.commit()
conn.close()