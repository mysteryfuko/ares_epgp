from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render(request,'index.html')

def epgp(request):
  data = {
    "data":[
      {"class":"DRUID","ep":"44444","gp":"222","name":"锤蛋"},
      {"class":"DRUID","ep":"44444","gp":"222","name":"锤蛋"}
    ]
  }
  return HttpResponse(json.dumps(data))
#ajax返回总ep奖励记录
def epgplog1(request):
  data = {
    "data":[
      {"time":"2020-06-17 09:30","name":"击杀XXXX","ep":"22","player":"18404","id":"1"},
      {"time":"2020-06-17 09:30","name":"击杀XXXX1","ep":"22","player":"12404","id":"2"},
    ]
  }
  return HttpResponse(json.dumps(data))

#ajax返回总ep拾取记录
def epgplog(request):
  data = {
    "data":[
      {"time":"2020-06-17 09:30","name":"锤蛋","class":"DRUID","gp":"222","item":"18404","active":"","active":""},
      {"time":"2020-06-17 09:30","name":"锤蛋","class":"DRUID","gp":"222","item":"12404","active":"","active":""},
    ]
  }
  return HttpResponse(json.dumps(data))

def dkp(request):
  data = {
    "data":[
      {"class":"DRUID","dkp":"44444","name":"锤蛋"},
      {"class":"DRUID","dkp":"3333","name":"锤蛋"}
    ]
  }
  return HttpResponse(json.dumps(data))

#ajax返回总dkp拾取记录
def dkplog(request):
  data = {
    "data":[
      {"time":"2020-06-17 09:30","name":"锤蛋","class":"DRUID","dkp":"222","item":"17404"},
      {"time":"2020-06-17 09:30","name":"锤蛋","class":"DRUID","dkp":"222","item":"13404"},
    ]
  }
  return HttpResponse(json.dumps(data))
#ajax返回总dkp奖励记录
def dkplog1(request):
  data = {
    "data":[
      {"time":"2020-06-17 09:30","name":"击杀XXXX","dkp":"22","player":"18404","id":"1"},
      {"time":"2020-06-17 09:30","name":"击杀XXXX1","dkp":"22","player":"12404","id":"2"},
    ]
  }
  return HttpResponse(json.dumps(data))
  
def PlayerDetail(request):
  return render(request,'PlayerDetail.html')

def Playerepgplog(request):
  data = {
    "data":[
      {"time":"2020-06-17 09:30","name":"锤蛋","ep":"","gp":"+250","item":"18404","activeID":"","active":""},
      {"time":"2020-06-17 10:30","name":"锤蛋","ep":"","gp":"+320","item":"12404","activeID":"","active":""},
      {"time":"2020-06-17 11:30","name":"锤蛋","ep":"+40","gp":"","item":"","activeID":"1","active":"加尔"}
    ]
  }
  return HttpResponse(json.dumps(data))

def Playerdkplog(request):
  data = {
    "data":[
      {"time":"2020-06-17 09:30","name":"锤蛋","dkp":"-20","item":"18404","activeID":"","active":""},
      {"time":"2020-06-17 10:30","name":"锤蛋","dkp":"-20","item":"12404","activeID":"","active":""},
      {"time":"2020-06-17 11:30","name":"锤蛋","dkp":"+5","item":"","activeID":"1","active":"加尔"}
    ]
  }
  return HttpResponse(json.dumps(data))

def kill(request):
  return render(request,'kill.html')