from django.shortcuts import render
from .models import score,record,user
import json
import datetime
from django.core import serializers
import os
from django.http import HttpResponse, Http404, FileResponse
import time
from point import do_report
from django.db.models import F,Q
import zipfile

from django.db import connection

def index(request):
    return render(request,'index.html')

def ajax(request,action):
  global where_to_do,num
  if action =="do_epgp":
    #备份
    new_name = "./backup/decay" + str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())) + ".zip"
    zp=zipfile.ZipFile(new_name,'w', zipfile.ZIP_DEFLATED)
    zp.write("db.sqlite3")
    zp.close()
    #操作
    epgp = score.objects.update(ep=F('ep')*0.9,gp=((F('gp')+300)*0.9-300))
    epgp1 = score.objects.filter(Q(gp__lt=0)).update(gp=0)
    decay_name = score.objects.all()
    decay_name_list = ""
    for i in decay_name:
      decay_name_list = decay_name_list + i.name + ","
    record.objects.create(boss="衰减10%", time=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),name = decay_name_list,ep=0,gp=0,dkp=0)
    return HttpResponse("done")

  if action == "do_report":
    url = request.POST["url"]
    print(url)
    if do_report.list_num == 1:
      do_report.where_to_do="开始分析"
      do_report.num = 0
      detail_list = do_report.get_fight_data(url)
    do_report.list_num = 1
    return HttpResponse(detail_list)

  if action == "do_status_report":
    dic = [(do_report.num/do_report.list_num)*100,do_report.where_to_do]
    return HttpResponse(json.dumps(dic))

  #ajax返回epgp列表
  if action == "epgp":
    epgp = score.objects.all()
    json_list = []
    for i in epgp:
      json_dict = {}
      json_dict["class"] = i.job
      json_dict["ep"] = str(i.ep)
      json_dict["gp"] = str(i.gp)
      json_dict["name"] = i.name
      json_list.append(json_dict)
    data ={"data":json_list}
    return HttpResponse(json.dumps(data))
  
  #ajax返回dkp列表
  if action == "dkp": 
    epgp = score.objects.all()
    json_list = []
    for i in epgp:
      json_dict = {}
      json_dict["class"] = i.job
      json_dict["dkp"] = i.dkp
      json_dict["name"] = i.name
      json_list.append(json_dict)
    data ={"data":json_list}
    return HttpResponse(json.dumps(data))

  #ajax返回epgp loot记录
  if action == "epgplootlog":
    KillLog = record.objects.filter(gp__isnull=False,item__isnull=False)
    json_list = []
    for i in KillLog:
      json_dict = {}
      json_dict["id"] = i.id      
      json_dict["item"] = i.item
      json_dict["gp"] = i.gp
      json_dict["class"] = score.objects.get(name=i.name).job
      json_dict["time"] = i.time.strftime("%Y-%m-%d %H:%M:%S")
      json_dict["name"] = i.name
      json_list.append(json_dict)
    data ={"data":json_list}
    return HttpResponse(json.dumps(data))

    #ajax返回总ep奖励记录 {,"ep":"22","player":"18404","},
  if action == "epgpaddlog":
    KillLog = record.objects.filter(boss__gt="").exclude(ep=0)
    KillLog1 = record.objects.filter(boss="衰减10%")
    json_list = []
    for i in KillLog1:
      json_dict = {}
      json_dict["id"] = i.id      
      json_dict["boss"] = i.boss
      json_dict["ep"] = i.ep
      json_dict["time"] = i.time.strftime("%Y-%m-%d %H:%M:%S")
      json_dict["player"] = len(i.name.split(','))
      json_list.append(json_dict)
    for i in KillLog:
      json_dict = {}
      json_dict["id"] = i.id      
      json_dict["boss"] = i.boss
      json_dict["ep"] = i.ep
      json_dict["time"] = i.time.strftime("%Y-%m-%d %H:%M:%S")
      json_dict["player"] = len(i.name.split(','))
      json_list.append(json_dict)
    data ={"data":json_list}
    return HttpResponse(json.dumps(data))

    #ajax返回dkp loot记录
  if action == "dkplootlog":
    KillLog = record.objects.filter(dkp__isnull=False,item__isnull=False)
    json_list = []
    for i in KillLog:
      json_dict = {}
      json_dict["id"] = i.id      
      json_dict["item"] = i.item
      json_dict["dkp"] = i.dkp
      json_dict["class"] = score.objects.get(name=i.name).job
      json_dict["time"] = i.time.strftime("%Y-%m-%d %H:%M:%S")
      json_dict["name"] = i.name
      json_list.append(json_dict)
    data ={"data":json_list}
    return HttpResponse(json.dumps(data))
    

      #ajax返回总dkp奖励记录
  if action == "dkpaddlog":
    KillLog = record.objects.filter(dkp__gt=0,boss__gt="")
    json_list = []
    for i in KillLog:
      json_dict = {}
      json_dict["id"] = i.id      
      json_dict["name"] = i.boss
      json_dict["dkp"] = i.dkp
      json_dict["time"] = i.time.strftime("%Y-%m-%d %H:%M:%S")
      json_dict["player"] = len(i.name.split(','))
      json_list.append(json_dict)
    data ={"data":json_list}

    return HttpResponse(json.dumps(data))


  if action == "Playerepgplog":
    name = request.GET["name"]
    logs = record.objects.extra(where=['("point_record"."ep" <> 0 AND "point_record"."name" LIKE "'+str(name)+',%%") OR ("point_record"."ep" <> 0 AND "point_record"."name" = "' + str(name) +'") OR ("point_record"."ep" <> 0 AND "point_record"."name" LIKE "%%,'+str(name)+',%%") OR ("point_record"."gp" <> 0 AND "point_record"."name" LIKE "'+str(name)+',%%") OR ("point_record"."gp" <> 0 AND "point_record"."name" = "' + str(name) +'") OR ("point_record"."gp" <> 0 AND "point_record"."name" LIKE "%%,'+str(name)+',%%") OR ("point_record"."ep" = 0 AND "point_record"."GP" = 0 AND "point_record"."dkp" = 0 AND "point_record"."name" LIKE "'+str(name)+',%%") OR ("point_record"."ep" = 0 AND "point_record"."GP" = 0 AND "point_record"."dkp" = 0 AND "point_record"."name" = "' + str(name) +'") OR ("point_record"."ep" = 0 AND "point_record"."GP" = 0 AND "point_record"."dkp" = 0 AND "point_record"."name" LIKE "%%,'+str(name)+',%%")'])
    json_list = []
    for i in logs:
      json_dict = {}
      json_dict["name"] = name
      json_dict["activeID"] = i.id      
      json_dict["time"] = i.time.strftime("%Y-%m-%d %H:%M:%S")
      json_dict["ep"] = i.ep
      json_dict["gp"] = i.gp
      json_dict["item"] = i.item 
      json_dict["active"] = i.boss 
      json_list.append(json_dict)
    data ={"data":json_list}

    return HttpResponse(json.dumps(data))

  if action == "Playerdkplog":
    name = request.GET["name"]
    nameid = score.objects.get(name=name).id
    logs = record.objects.extra(where=['"point_record"."dkp" <> 0 AND "point_record"."name" LIKE "'+str(name)+',%%") OR ("point_record"."dkp" <> 0 AND "point_record"."name" = "' + str(name) +'") OR("point_record"."dkp" <> 0 AND "point_record"."name" LIKE "%%,'+str(name)+',%%"'])
    json_list = []
    for i in logs:
      json_dict = {}
      json_dict["name"] = name
      json_dict["activeID"] = i.id      
      json_dict["time"] = i.time.strftime("%Y-%m-%d %H:%M:%S")
      json_dict["dkp"] = i.dkp
      json_dict["item"] = i.item 
      json_dict["active"] = i.boss 
      json_list.append(json_dict)
    data ={"data":json_list}
    return HttpResponse(json.dumps(data))

def PlayerDetail(request,name):
  return render(request,'PlayerDetail.html',{"name":name})

  
def kill(request,bossid):
  KillLog = record.objects.get(id=int(bossid))
  name = KillLog.name.split(',')
  renderData = {
    "id":bossid,
    "time":KillLog.time,
    "boss":KillLog.boss,
    "ep":KillLog.ep,
    "dkp":KillLog.dkp,
    "name":name
  }
  #print(renderData)
  return render(request,'kill.html',renderData)

def down(request):
  epgp = score.objects.all()
  json_dict = "WebDKP_DkpTable = {\n"
  for i in epgp:
    json_dict =json_dict + '["'+i.name+'"]={\n\t["class"]="'
    json_dict =json_dict + i.job + '",\n\t["online"]=true,\n\t["dkp"]='
    json_dict= json_dict + str(i.dkp) + ',\n\t["dkp_1"]=' +str(i.dkp)+',\n\t["dkp_lifetime_1"]='+str(i.dkp)+',\n},\n'
  json_dict = json_dict + '}\nWebDKP_Tables = {\n["BWL"] = {\n		["id"] = 1, \n},\n}\n\nWebDKP_Loot = {\n}\n\nWebDKP_Alts = {\n}\n\nWebDKP_WebOptions = {\n["ZeroSumEnabled"] = 0,\n\n["CombineAlts"] = 1,\n["TiersEnabled"] = 1,\n["TierSize"] = 50,\n["LifetimeEnabled"] = 1,\n["User"] = "mysteryfuko",\n["AddonVersion"] = 3,\n["WowCatSign"] = "04f91db9576bc71b04a06a3db5e9e4a4",\n}'
  response = FileResponse(json_dict)
  response['content_type'] = "application/octet-stream"
  response['Content-Disposition'] = 'attachment; filename=webDKP.lua'
  return response