import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import tkinter
root=tkinter.TK()
root.geometry
exq={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"}
a=requests.get("https://www.maigoo.com/news/651449.html",headers=exq)
if a.status_code == 200:  
    soup=BeautifulSoup(a.text,'html.parser')
    itr=soup.find_all('tr')
    biglist=[]
    for it in itr:
        flist=[]
        itd=it.find_all('td')
        for id in itd:
            flist.append(id.string)
        biglist.append(flist)
else:
    print("网站请求失败")

with open("CCD.csv",'w', newline='')as cfile:
    some=csv.writer(cfile)
    some.writerows(biglist)

df=pd.read_csv("CCD.csv",encoding='ansi')
print(df)


    
    
    
    
