# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 05:53:55 2023

@author: Sachin Kansal
"""

from urllib import request as req
from bs4 import BeautifulSoup as bs
import pandas as pd
#import numpy as np
#import datetime
date=str(200901) #yearmonth -- yyyymm
url="https://www.estesparkweather.net/archive_reports.php?date="+date

def link_maker(url,gt,lt):  # get the list of all month having value greater than gt and less than lt inclusive
    opener=req.urlopen(url)
    page=bs(opener,features='html.parser')
    ls1=page.form.findAll('option')
    ls2=[]
    for i in ls1:
        a=i.attrs['value']
        if int(a)>=gt and int(a)<=lt:
            ls2.append(a)
    return ls2

def data_month(datem): #get data of everyday of each month
    dataframe=pd.DataFrame(columns=range(20))
    url="https://www.estesparkweather.net/archive_reports.php?date="+datem
    opener=req.urlopen(url)
    page=bs(opener,features='html.parser')

    k=page.find('div',attrs={'id':'main-copy'}).find_all('table')
    del k[-1]
    del k[-1]
    datem='-'+datem[4:]+'-'+datem[:4]
    date=1
    ls=[]
    for i in k:
        rows=i.find_all('tr')
        for j in rows:
            c=j.find_all('td')
            for n in c[-1]:
                if n.text[0]==' ':
                    ls.append(n.text)
        ls.append(str(date)+datem)
        dataframe.loc[len(dataframe)]=ls
        date=date+1
        ls.clear()
    return dataframe

#main 
link_list=link_maker(url, 200901, 200912) #get the list of all links to be crawled  from initial page
u_data=pd.DataFrame(columns=range(20)) #empty dataframe
for i in link_list: #iterate over list to get data of each month
    data=data_month(i) #data of each month
    u_data=pd.concat([u_data,data],axis=0) # data of each month updated/stored in final on dataframe 
del data, i, date, link_list
u_data=u_data.set_index(19)
