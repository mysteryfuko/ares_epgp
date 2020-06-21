from django.shortcuts import render
from django.http import HttpResponse
from .models import score,record
import json
import datetime
from django.core import serializers


def index(request):
    return render(request,'index.html')

def ajax(request,action):
  #ajax返回epgp列表
  if action == "epgp":
    epgp = score.objects.all()
    json_list = []
    for i in epgp:
      json_dict = {}
      json_dict["class"] = i.job
      json_dict["ep"] = i.ep
      json_dict["gp"] = i.gp
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
      json_dict["class"] = score.objects.get(id=i.name).job
      json_dict["time"] = i.time.strftime("%Y-%m-%d %H:%M:%S")
      json_dict["name"] = score.objects.get(id=i.name).name
      json_list.append(json_dict)
    data ={"data":json_list}
    return HttpResponse(json.dumps(data))

    #ajax返回总ep奖励记录 {,"ep":"22","player":"18404","},
  if action == "epgpaddlog":
    KillLog = record.objects.filter(ep__isnull=False,boss__gt="")
    json_list = []
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
      json_dict["class"] = score.objects.get(id=i.name).job
      json_dict["time"] = i.time.strftime("%Y-%m-%d %H:%M:%S")
      json_dict["name"] = score.objects.get(id=i.name).name
      json_list.append(json_dict)
    data ={"data":json_list}
    return HttpResponse(json.dumps(data))
    

      #ajax返回总dkp奖励记录
  if action == "dkpaddlog":
    KillLog = record.objects.filter(dkp__isnull=False,boss__gt="")
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
    nameid = score.objects.get(name=name).id
    logs = record.objects.extra(where=['"point_record"."dkp" IS NULL AND "point_record"."name" LIKE "'+str(nameid)+',%%") OR ("point_record"."dkp" IS NULL AND "point_record"."name" = "' + str(nameid) +'") OR("point_record"."dkp" IS NULL AND "point_record"."name" LIKE "%%,'+str(nameid)+',%%"'])
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
    logs = record.objects.extra(where=['"point_record"."dkp" IS NOT NULL AND "point_record"."name" LIKE "'+str(nameid)+',%%") OR ("point_record"."dkp" IS NOT NULL AND "point_record"."name" = "' + str(nameid) +'") OR("point_record"."dkp" IS NOT NULL AND "point_record"."name" LIKE "%%,'+str(nameid)+',%%"'])
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
  Playername = []
  for i in name:
    json_dict = {}
    json_dict["id"] = i
    Playername.append(score.objects.get(id=i).name)
  renderData = {
    "id":bossid,
    "time":KillLog.time,
    "boss":KillLog.boss,
    "ep":KillLog.ep,
    "dkp":KillLog.dkp,
    "name":Playername
  }
  #print(renderData)
  return render(request,'kill.html',renderData)