import requests  
from bs4 import BeautifulSoup  
import csv
import numpy as np
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
from tkinter.messagebox import *

print("开始......")

mtn=0

def no1():
    global mtn
    mtn+=3
    exq = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"}  
    a = requests.get("https://www.maigoo.com/news/662215.html",headers=exq)
    a.encoding = a.apparent_encoding
    if a.status_code == 200:    
        soup = BeautifulSoup(a.text, 'html.parser')  
        itr = soup.find_all('tr')  
        biglist = []  
        for it in itr:  
            flist = []  
            itd = it.find_all('td')  
            for id in itd:   
                flist.append(id.get_text(strip=True, separator=' '))  
            if flist:   
                biglist.append(flist)  
    else:  
        messagebox.showinfo(title='提示', message="网络请求错误")    
        return  
  
    with open("CCD.csv", 'w', newline='') as cfile:  
        some = csv.writer(cfile)  
        some.writerows(biglist)
    messagebox.showinfo(title='提示',message="数据已保存为CSV文件！")
    df = pd.read_csv("CCD.csv", encoding='ansi')    
def no2():
    global mtn
    mtn=2
    file_path = 'CCD.csv'
    top_100_rows = []
    with open(file_path, 'r', newline='') as file:
         reader = csv.reader(file)
         for i, row in enumerate(reader):
            if i < 101:
                 if i < 100:
                    top_100_rows.append(row)
                 else:
                     row[0]=100
                     top_100_rows.append(row)       
    with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(top_100_rows)

    messagebox.showinfo(title='提示',message="处理后数据已保存！")
def no3(databox):
    finame=r'CCD.csv'
    df=pd.read_csv(finame,encoding='ansi')
    df1=df.head(100)

    df1_rows=df1.to_numpy().tolist()
    title=['1','2','3','4','5']
    column=['名次','学校名称','省市','类型','总分']
    for col in title:
        databox.column(col,width=90,anchor='center')
    i=0
    for colu in column:
        databox.heading(title[i],text=colu)
        i=i+1
    for row in df1_rows:
        databox.insert('','end',values=row)
def no4():
    hh=Toplevel()
    hh.title("统计方式")
    hh.geometry("300x300")
    lb1=tk.Label(hh,text="请选择统计方式",fg='red').place(x=35,y=10)
    but41=tk.Button(hh,text="统计各省高校数量",command=no41).place(x=90,y=55)
    but42=tk.Button(hh,text="统计各类型各省数量",command=no42).place(x=90,y=155)
    mainloop()
    
def no41():
    df = pd.read_csv('CCD.csv',encoding='ansi')
    prov = df.groupby('省市')['学校名称'].count().reset_index(name='数量')
    provi= prov.sort_values(by='数量', ascending=False)
    formatted_output = provi.to_string(index=False, header=True)  
    messagebox.showinfo(title='统计结果',message=formatted_output)

def no42():
    df = pd.read_csv('CCD.csv',encoding='ansi')
    province_type_counts = df.groupby(['省市', '类型'])['学校名称'].count().reset_index(name='数量')
    pppp = province_type_counts.sort_values(by='数量', ascending=False)
    formatted_output2 = pppp.to_string(index=False, header=True)  
    messagebox.showinfo(title='统计结果',message=formatted_output2)

def no5():
    jj=Toplevel()
    jj.title("视图")
    jj.geometry("300x300")
    lb1=tk.Label(jj,text="请选择视图方式",fg='red').place(x=35,y=10)
    but41=tk.Button(jj,text="各省Top100民办高校数量柱状图",command=no51).place(x=90,y=55)
    but42=tk.Button(jj,text="不同类型高校百分比扇形图",command=no52).place(x=90,y=155)
    mainloop()
    

def no51(): 
      
    df = pd.read_csv('CCD.csv', encoding='ansi')   
      
    province_counts = df['省市'].value_counts().reset_index()  
    province_counts.columns = ['省市', '高校数量']  
      
    plt.rcParams['font.sans-serif'] = ['SimHei']   
    plt.rcParams['axes.unicode_minus'] = False    
    fig, ax = plt.subplots(figsize=(10, 6))   
    bars = ax.bar(province_counts['省市'], province_counts['高校数量'], color='skyblue')  
      
    def add_numbers(bars, ax):  
        for bar in bars:  
            height = bar.get_height()  
            if height > 0: 
                ax.annotate(f'{height}',   
                            xy=(bar.get_x() + bar.get_width() / 2, height),  
                            xytext=(0, 3),    
                            textcoords="offset points",  
                            ha='center', va='bottom')  
      
    add_numbers(bars, ax)  
      
    ax.set_title('各省Top100民办高校数量')  
    ax.set_xlabel('省市')  
    ax.set_ylabel('高校数量')  
 
    plt.tight_layout()   
    plt.show()

def no52():
    df = pd.read_csv('CCD.csv', encoding='ansi')  # 替换为你的CSV文件名
    type_counts = df['类型'].value_counts()

    total_count = len(df)


    type_percentages = (type_counts / total_count) * 100

   
    plt.rcParams['font.sans-serif'] = ['SimHei']  
    plt.rcParams['axes.unicode_minus'] = False 

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(type_percentages, labels=type_counts.index, autopct='%1.1f%%')
    ax.set_title('不同类型高校百分比扇形图')
    plt.show()

       
def cse1():  
    no1()

def cse2():
    if mtn==0:
        messagebox.showinfo(title='提示',message="请先获取数据！")
    else:
        no2()
def cse3():
    if mtn==0:
        messagebox.showinfo(title='提示',message="请先获取数据！")
    else:
        no3(databox)
def cse4():
    if mtn==2:
        no4()
    else:
        messagebox.showinfo(title='提示',message="请先获取并处理数据！")
def cse5():
    if mtn==2:
        no5()
    else:
        messagebox.showinfo(title='提示',message="请先获取并处理数据！")

        
root=tk.Tk()
root.title('综合实验')
root.geometry("600x600")
Frame(root, width=120, height=400, bg='pink',padx=100, pady=10).place(x=5,y=85)
Frame(root, width=400, height=350, bg='lightblue').place(x=145,y=85)

what =tk.Button(root, text="获取并保存数据", command=cse1).place(x=15,y=95)
can  =tk.Label(root,text="控 制 台").place(x=35,y=60)
I    =tk.Button(root,text="处理并保存数据",command=cse2).place(x=15,y=155)
say  =tk.Label(root,text="中国民办高校数据统计与可视化",font=('黑体',25),fg='blue').place(x=79,y=20)

but3 =tk.Button(root,text='显示学校信息',command=cse3).place(x=250,y=450)
but4 =tk.Button(root,text="   数据统计    ",command=cse4).place(x=15,y=215)
but4 =tk.Button(root,text="   数据可视化    ",command=cse5).place(x=15,y=275)

title=['1','2','3','4','5']
databox=ttk.Treeview(root,columns=title,show='headings')
databox.place(x=150,y=90,width=390,height=340)


status_frame = tk.Frame(root, height=20, bd=1, relief=tk.SUNKEN)  
status_frame.pack(side=tk.BOTTOM, fill=tk.X)
statusbar = tk.Label(status_frame, text="就绪", anchor=tk.W)   
statusbar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
 

root.mainloop()

