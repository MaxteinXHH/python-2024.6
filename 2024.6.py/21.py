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
import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# 假设你已经有了一个DataFrame 'df'
df = pd.read_csv('CCD.csv', usecols=['名次', '名字', '财富', '财富来源', '国家/地区'])

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.RangeSlider(
        id='wealth-slider',
        min=df['财富'].min(),
        max=df['财富'].max(),
        value=[df['财富'].min(), df['财富'].max()],
        marks={str(round(i, 2)): str(round(i, 2)) for i in range(df['财富'].min(), df['财富'].max()+1, 1000000000)},  # 假设财富单位是美元
        step=100000000  # 假设步长为1亿美元
    ),
    dcc.Graph(id='billionaire-graph')
])

@app.callback(
    Output('billionaire-graph', 'figure'),
    Input('wealth-slider', 'value')
)
def update_graph(selected_wealth_range):
    filtered_df = df[(df['财富'] >= selected_wealth_range[0]) & (df['财富'] <= selected_wealth_range[1])]
    
    # 创建图表（这里以散点图为例）
    fig = go.Figure(data=[go.Scatter(x=filtered_df['名字'], y=filtered_df['财富'], mode='markers', text=filtered_df['国家/地区'])])
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
def no1():
    global mtn
    mtn+=3
    exq = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"}  
    a = requests.get("https://www.phb123.com/renwu/fuhao/shishi.html",headers=exq)
    a.encoding = a.apparent_encoding
    if a.status_code == 200:    
        soup = BeautifulSoup(a.text, 'html.parser')  
        itr = soup.find_all('tr')
        biglist=[]
        ilist=['名次','名字','财富','财富来源','国家/地区']
        biglist.append(ilist)
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
    
    can2.destroy()
    finame=r'CCD.csv'
    df=pd.read_csv(finame,encoding='ansi')
    df1=df.head(100)

    df1_rows=df1.to_numpy().tolist()
    title=['1','2','3','4','5']
    column=['名次','名字','财富','财富来源','国家/地区']
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
    but41=tk.Button(hh,text="统计各国家富豪数量",command=no41).place(x=90,y=55)
    but42=tk.Button(hh,text="统计各各国家富豪财富总量",command=no42).place(x=90,y=155)
    mainloop()
    
def no41():
    df = pd.read_csv('CCD.csv',encoding='ansi')
    prov = df.groupby('国家/地区')['名字'].count().reset_index(name='数量')
    provi= prov.sort_values(by='数量', ascending=False)
    formatted_output = provi.to_string(index=False, header=True)  
    messagebox.showinfo(title='各国家富豪数量',message=formatted_output)

def no42():
    df = pd.read_csv('CCD.csv',encoding='ansi')
    df['财富'] = df['财富'].str.replace('亿美元', '').astype(float)
    wealth_summary = df.groupby('国家/地区')['财富'].sum().reset_index()
    result_string = "各个国家富豪财富总量统计：\n"
    for index, row in wealth_summary.iterrows():
        result_string += f"{row['国家/地区']}: {row['财富']:.2f}亿美元\n"
    messagebox.showinfo(title='各国家富豪财富总量',message=result_string)

def no5():
    jj=Toplevel()
    jj.title("视图")
    jj.geometry("300x300")
    lb1=tk.Label(jj,text="请选择视图方式",fg='red').place(x=35,y=10)
    but41=tk.Button(jj,text="各个国家富豪财富总量柱状图",command=no51).place(x=90,y=55)
    but42=tk.Button(jj,text="各国富豪财富总量扇形对比图",command=no52).place(x=90,y=155)
    mainloop()
    

def no51(): 
      
    df = pd.read_csv('CCD.csv', encoding='ansi')
    df['财富'] = df['财富'].str.replace('亿美元', '').astype(float)
    wealth_summary = df.groupby('国家/地区')['财富'].sum().reset_index()
    wealth_summary.sort_values(by='财富', ascending=False, inplace=True)
    plt.figure(figsize=(12, 7))
    plt.rcParams['font.sans-serif'] = ['SimHei'] 
    plt.rcParams['axes.unicode_minus'] = False 
    bar_positions = range(len(wealth_summary))
    bar_heights = wealth_summary['财富']
    plt.bar(bar_positions, bar_heights, tick_label=wealth_summary['国家/地区'])
    for i, v in enumerate(bar_heights):
        plt.text(i, v + 1, f'{v}', va='bottom', ha='center')  
    plt.text(0.5,1.1, '各国富豪财富总量柱状图', ha='center', fontsize=22, transform=plt.gca().transAxes)
    plt.ylabel('财富总量（亿美元）')
    plt.show()

def no52():
    df = pd.read_csv('CCD.csv', encoding='ansi') 
    df['财富'] = df['财富'].str.replace('亿美元', '').astype(float)
    wealth_summary = df.groupby('国家/地区')['财富'].sum().reset_index()
    wealth_summary['百分比'] = wealth_summary['财富'] / wealth_summary['财富'].sum() * 100
    plt.rcParams['font.sans-serif'] = ['SimHei'] 
    plt.rcParams['axes.unicode_minus'] = False  
    plt.figure(figsize=(10, 7))
    plt.pie(wealth_summary['百分比'], labels=wealth_summary['国家/地区'], autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.text(0.5,1.1, '各国富豪财富总量扇形对比图', ha='center', fontsize=22, transform=plt.gca().transAxes)
    plt.show()
 

       
def cse1():  
    no1()  

                                                                              
def cse2():
    if mtn==0:
        messagebox.showwarning(title='警告:',message="请先获取数据！")
    else:
        no2()
def cse3():
    if mtn==0:
        messagebox.showwarning(title='警告:',message="请先获取数据！")
    else:
        no3(databox)
def cse4():
    if mtn==2:
        no4()
    else:
        messagebox.showwarning(title='警告:',message="请先获取并处理数据！")
def cse5():
    if mtn==2:
        no5()
    else:
        messagebox.showwarning(title='警告:',message="请先获取并处理数据！")

        
root=tk.Tk()
root.title('综合实验')
root.geometry("600x600")
Frame(root, width=120, height=400, bg='pink',padx=100, pady=10).place(x=5,y=85)
Frame(root, width=400, height=350, bg='lightblue').place(x=145,y=85)

what =tk.Button(root, text="获取并保存数据", command=cse1).place(x=15,y=95)
can  =tk.Label(root,text="控 制 台").place(x=35,y=60)
I    =tk.Button(root,text="处理并保存数据",command=cse2).place(x=15,y=155)
say  =tk.Label(root,text="福布斯全球富豪榜实时数据分析系统",font=('黑体',22),fg='blue').place(x=49,y=20)

but3 =tk.Button(root,text='    显示排行信息    ',command=cse3).place(x=250,y=450)
but4 =tk.Button(root,text="   数据统计    ",command=cse4).place(x=15,y=215)
but4 =tk.Button(root,text="   数据可视化    ",command=cse5).place(x=15,y=275)
but5 =tk.Button(root,text="",command=cse5).place(x=1,y=1,width=3,height=2)



title=['1','2','3','4','5']
databox=ttk.Treeview(root,columns=title,show='headings')
databox.place(x=150,y=90,width=390,height=340)

print(pd['国家/地区'])

can2=tk.Label(root,text="就绪....",font=('黑体',15),bg='white')
can2.place(x=155,y=95)
status_frame = tk.Frame(root, height=20, bd=1, relief=tk.SUNKEN)  
status_frame.pack(side=tk.BOTTOM, fill=tk.X)
statusbar = tk.Label(status_frame, text="就绪", anchor=tk.W)   
statusbar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

root.mainloop()

