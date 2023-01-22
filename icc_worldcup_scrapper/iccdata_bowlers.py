# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 00:48:09 2023

@author: Sachin Kansal
"""
#%% webscrapper1   icc bowling averages
from urllib import request as req
from bs4 import BeautifulSoup as BS
import numpy as nm
import pandas as pd
from pandas import Series, DataFrame
import csv

url="https://stats.espncricinfo.com/ci/engine/records/averages/bowling.html?id=89;team=6;type=trophy"
page= req.urlopen(url)
#print(page.status_code)
bs_obj=BS(page.read(),features="html.parser")
table_ls=bs_obj.findAll('table',attrs={'class':"engineTable"})
for i in table_ls:
    if i.caption!=None:
        dat_table=i
        del table_ls
        break
# dat_table --> required table
print(dat_table.caption)
# titles list
titles=dat_table.thead.tr.find_all('th')
titles_list=[]
for i in titles:
    titles_list.append(i.attrs['title'])
del titles
titles_list.append('href')
csvfile=open('iccdata.csv','w+')
ls=[]
writer= csv.writer(csvfile)
writer.writerow(titles_list)
data_raw=dat_table.tbody.findAll('tr')
for i in data_raw:
    r=i.findAll('td')
    for j in r:
        ls.append(j.text)
    ls.append(i.td.a.attrs['href'])
    writer.writerow(ls)
    ls.clear()
del ls, titles_list, writer, r
csvfile.close()

data=pd.read_csv('iccdata.csv')
