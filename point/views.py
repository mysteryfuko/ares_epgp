from django.shortcuts import render
from django.http import HttpResponse
from .models import score,record
from django.core import serializers
import json

class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime.datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, datetime.date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj)

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
    data = {
      "data":[
        {"time":"2020-06-17 09:30","name":"锤蛋","ep":"","gp":"+250","item":"18404","activeID":"","active":""},
        {"time":"2020-06-17 10:30","name":"锤蛋","ep":"","gp":"+320","item":"12404","activeID":"","active":""},
        {"time":"2020-06-17 11:30","name":"锤蛋","ep":"+40","gp":"","item":"","activeID":"1","active":"加尔"}
        ]
      }
    return HttpResponse(json.dumps(data))

  if action == "Playerdkplog":
    data = {
      "data":[
        {"time":"2020-06-17 09:30","name":"锤蛋","dkp":"-20","item":"18404","activeID":"","active":""},
        {"time":"2020-06-17 10:30","name":"锤蛋","dkp":"-20","item":"12404","activeID":"","active":""},
        {"time":"2020-06-17 11:30","name":"锤蛋","dkp":"+5","item":"","activeID":"1","active":"加尔"}
        ]
      }
    return HttpResponse(json.dumps(data))


  return HttpResponse(json.dumps(data))
  
def PlayerDetail(request,**keyword ):
  return render(request,'PlayerDetail.html')

  

def kill(request,id):
  return HttpResponse(id)