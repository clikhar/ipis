from django.shortcuts import render
from django.http import HttpResponse
from pandas.core.indexing import maybe_convert_ix
from .models import Train_Data, Train_Coach

import time
import requests
import json
import html
import csv
import pandas as pd
from  pythonping  import ping

station = 'NGP'
# Create your views here.
def home(request):
    ntes_data = mix_data()
    json_ntes_data = json.dumps(ntes_data)
    return render(request,'TV_Display_English.html',{'ntes_data':ntes_data,'station':station,'json_ntes_data':json_ntes_data})

def home2(request):
    ntes_data = mix_data2()
    json_ntes_data = json.dumps(ntes_data)
    return render(request,'TV_Display_English2.html',{'ntes_data':ntes_data,'station':station,'json_ntes_data':json_ntes_data})

def hindi(request):
    ntes_data = mix_data()
    json_ntes_data = json.dumps(ntes_data)
    return render(request,'TV_Display_Hindi.html',{'ntes_data':ntes_data,'station':station,'json_ntes_data':json_ntes_data})

def hindi2(request):
    ntes_data = mix_data2()
    json_ntes_data = json.dumps(ntes_data)
    return render(request,'TV_Display_Hindi2.html',{'ntes_data':ntes_data,'station':station,'json_ntes_data':json_ntes_data})
       
def marathi(request):
    ntes_data = mix_data()
    json_ntes_data = json.dumps(ntes_data)
    return render(request,'TV_Display_Marathi.html',{'ntes_data':ntes_data,'station':station,'json_ntes_data':json_ntes_data})

def tv_java(request):
    ntes_data =  mix_data()
    json_ntes_data = json.dumps(ntes_data)
    return render(request,'TV_Display_Java.html',{'ntes_data':ntes_data,'station':station,'json_ntes_data':json_ntes_data})

def ntes_display_format(request):
    ntes_data= data()
    json_ntes_data = json.dumps(ntes_data)
    return render(request,'NTES_TV_Display_English.html',{'ntes_data':ntes_data,'station':station,'json_ntes_data':json_ntes_data})     

def ntes_display_java(request):
    ntes_data= data()
    json_ntes_data = json.dumps(ntes_data)
    return render(request,'NTES_TV_Display_Java.html',{'ntes_data':ntes_data,'station':station,'json_ntes_data':json_ntes_data})     

def login(request):
    ntes_data = data()
    json_ntes_data = json.dumps(ntes_data)
    return render(request,'login.html',{'ntes_data':ntes_data,'station':station,'json_ntes_data':json_ntes_data})

def tenline(request):
    ntes_data = file_data()
    json_ntes_data = json.dumps(ntes_data)
    return render(request,'10LINE.html',{'ntes_data':ntes_data,'station':station,'json_ntes_data':json_ntes_data})

def tenlineH(request):
    ntes_data = file_data()
    json_ntes_data = json.dumps(ntes_data)
    return render(request,'10LINE_H.html',{'ntes_data':ntes_data,'station':station,'json_ntes_data':json_ntes_data})

def tenlineM(request):
    ntes_data = file_data()
    json_ntes_data = json.dumps(ntes_data)
    return render(request,'10LINE_M.html',{'ntes_data':ntes_data,'station':station,'json_ntes_data':json_ntes_data})

def data():
    #url = 'https://enquiry.indianrail.gov.in/ntessrvc/TrainService?action=LiveStation'
    url = 'https://enquiry.indianrail.gov.in/ntessrvc/LiveStation'
    body = {"station":station,"nextMins":480}
    headers = {'authToken': '569a6d6c430c906e98ad192e6ea0cd51'}

    r = requests.post(url, data=json.dumps(body), headers=headers)
    #print(r.json()['vTrainList'][0]['trainNo'])
    ntes_data = r.json()['vTrainList']
    train_list = []
    i = 0
    for train_data in ntes_data:
        if i<10:
            
            train_data['trainNameHindi']=  html.unescape(train_data['trainNameHindi'])
            train_data['ETA']=  train_data['ETA'][-5:]
            train_data['ETD']=  train_data['ETD'][-5:]
            train_list.append(train_data)
            i= i + 1
        
    return train_list

def file_data():

    jsonArray = []
    #csvFilePath = 'C:\\Users\\ssetelestn\\Desktop\\BOT\\TRN_For_TV_4.txt'
    #csvFilePath= '\\\\192.168.1.253\\Users\\Public\\TRN_For_TV_4.txt'  

    #to check connectivity of Master and Slave PC
    try:
        response =ping("192.168.1.253")
        response2 =ping("192.168.1.254")
        if response.rtt_min_ms != 2000:
            csvFilePath= '\\\\192.168.1.253\\Users\\Public\\TRN_For_TV_4.txt'
            
        elif response2.rtt_min_ms != 2000:
            csvFilePath= '\\\\192.168.1.254\\Users\\Public\\TRN_For_TV_4.txt'
            
        else:
            csvFilePath="C:\\Users\\Public\\TRN_For_TV_4.txt"
            
    except:
        csvFilePath=""

    
    
    #read csv file
    try:
        with open(csvFilePath, encoding='utf-8') as csvf: 
            #load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf,fieldnames= ["BOARD","TNo","TNAMEE","AT","DT","AD","STAT","DELAY","EAT","EDT","PF","COACH","TNAMEH","TNAMEM","STATH","STATM","a"], delimiter='\t',quoting=csv.QUOTE_NONE)
            next(csvReader)
            i = 0
            #print (csvReader.fieldnames)
            #convert each csv row into python dict
            for row in csvReader:            
                #add this python dict to json array
                if i<11:
                    jsonArray.append(row)
                i=i+1
        jsonArray.pop(-1)
        
        train_list = []
        i = 0
        for train_data in jsonArray:
            if i<10:              
                train_data['TNAMEM']=  train_data['TNAMEM'][0:32]
                train_data['TNAMEH']=  train_data['TNAMEH'][0:32]
                train_list.append(train_data)
                i= i + 1
            
        return train_list
    

    except:
        jsonArray.append("")


def mix_data():

    jsonArray = []
    #csvFilePath = 'C:\\Users\\ssetelestn\\Desktop\\BOT\\TRN_For_TV_4.txt'
    #csvFilePath= '\\\\192.168.1.253\\Users\\Public\\TRN_For_TV_4.txt'  

    #to check connectivity of Master and Slave PC
    try:
        response =ping("192.168.1.253")
        response2 =ping("192.168.1.254")
        if response.rtt_min_ms != 2000:
            csvFilePath= '\\\\192.168.1.253\\Users\\Public\\TRN_For_TV_4.txt'
            
        elif response2.rtt_min_ms != 2000:
            csvFilePath= '\\\\192.168.1.254\\Users\\Public\\TRN_For_TV_4.txt'
            
        else:
            csvFilePath="C:\\Users\\Public\\TRN_For_TV_4.txt"
            #csvFilePath=""
            
    except:
        csvFilePath=""

    
    
    #read csv file
    try:
        with open(csvFilePath, encoding='utf-8') as csvf: 
            #load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf,fieldnames= ["BOARD","trainNo","trainName","AT","DT","AD","STAT","DELAY","ETA","ETD","platformNo","coachPosition","trainNameHindi","trainNameMarathi","STATH","STATM","a"], delimiter='\t',quoting=csv.QUOTE_NONE)
            next(csvReader)
            i = 0
            #print (csvReader.fieldnames)
            #convert each csv row into python dict
            for row in csvReader:            
                #add this python dict to json array
                if i<11:
                    jsonArray.append(row)
                i=i+1
        jsonArray.pop(-1)
        
        train_list = []
        i = 0
        for train_data in jsonArray:
            if i<10:

                train_data['trainNameMarathi']=  train_data['trainNameMarathi'][0:32]
                train_data['trainNameHindi']=  train_data['trainNameHindi'][0:32]
                train_data['platformNo']=  train_data['platformNo'][-1:]
                train_list.append(train_data)
                i= i + 1
            
        return train_list
    

    except:
        jsonArray.append("")


def mix_data2():

    jsonArray = []
    #csvFilePath = 'C:\\Users\\ssetelestn\\Desktop\\BOT\\TRN_For_TV_4.txt'
    #csvFilePath= '\\\\192.168.1.253\\Users\\Public\\TRN_For_TV_4.txt'  

    #to check connectivity of Master and Slave PC
    try:
        response =ping("192.168.1.253")
        response2 =ping("192.168.1.254")
        if response.rtt_min_ms != 2000:
            csvFilePath= '\\\\192.168.1.253\\Users\\Public\\TRN_For_TV_4.txt'
            
        elif response2.rtt_min_ms != 2000:
            csvFilePath= '\\\\192.168.1.254\\Users\\Public\\TRN_For_TV_4.txt'
            
        else:
            csvFilePath="C:\\Users\\Public\\TRN_For_TV_4.txt"
            #csvFilePath=""
            
    except:
        csvFilePath=""

    
    
    #read csv file
    try:
        with open(csvFilePath, encoding='utf-8') as csvf: 
            #load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf,fieldnames= ["BOARD","trainNo","trainName","AT","DT","AD","STAT","DELAY","ETA","ETD","platformNo","coachPosition","trainNameHindi","trainNameMarathi","STATH","STATM","a"], delimiter='\t',quoting=csv.QUOTE_NONE)
            next(csvReader)
            i = 0
            #print (csvReader.fieldnames)
            #convert each csv row into python dict
            for row in csvReader:            
                #add this python dict to json array
                if i<11:
                    jsonArray.append(row)
                i=i+1
        jsonArray.pop(-1)
        
        train_list = []
        i = 0
        for train_data in jsonArray:
            if i<7:

                train_data['trainNameMarathi']=  train_data['trainNameMarathi'][0:32]
                train_data['trainNameHindi']=  train_data['trainNameHindi'][0:32]
                train_data['platformNo']=  train_data['platformNo'][-1:]
                train_list.append(train_data)
                i= i + 1
            
        return train_list
    

    except:
        jsonArray.append("")