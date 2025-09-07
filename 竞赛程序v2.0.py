#席hd

#联系我 https://maxteinxhh.github.io/fun/xhd.html

#我的网站 https://maxteinxhh.github.io/Xis-haohao/web/xishao.html

#  2024.6 python竞赛作品。

#这是一个使用 Python 编写的竞赛程序 v2.0.py ，主要用于对福布斯全球富豪榜实时数据进行分析和展示

#演示视频请移至
# https://www.bilibili.com/video/BV1pXYGz3EED/?share_source=copy_web







import requests
import re
from bs4 import BeautifulSoup  
import csv
import numpy as np
import pandas as pd
import tkinter as tk
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import tkinter
import tkinter.ttk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
from tkinter.messagebox import *
import webbrowser


#********          我拥有该代码和所有内容的所有权。为了方便您使用我们的内容，我们授予您特定的参阅权利，但您只能以我们允许的方式使用我们的内容。     *************
、
print("开始......")


mtn3=1

mtn=0

mtn2=1
def no1():
    statusbar.config(text="开始...")
    global mtn
    mtn=1
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
    statusbar.config(text="开始...原始数据已保存为'CCD.csv' ...")
    df = pd.read_csv("CCD.csv", encoding='ansi')


   
def no2():
    global mtn
    mtn=2
    
    df = pd.read_csv("CCD.csv", encoding='ansi')  
    df['财富来源'] = df['财富来源'].astype(str) 
    df['财富来源'] = df['财富来源'].apply(lambda x: '其他' if pd.isnull(x) or x.strip() == '' or x.strip() == 'nan' else x.strip()) 
    df.to_csv('CCD.csv', index=False, encoding='ansi')      

    messagebox.showinfo(title='提示',message="处理后数据已保存！")
    statusbar.config(text="开始...数据已处理,已保存为'CCD.csv' ...")
    
def no3(databox):

    a=var.get()
    
    can2.destroy()
    items = databox.get_children('')    
    for item in items:  
        databox.delete(item) 
    finame=r'CCD.csv'
    df=pd.read_csv(finame,encoding='ansi')
    df1=df.head(100)

    df1_rows=df1.to_numpy().tolist()
    title=['1','2','3','4','5']
    column=['全球名次','名字','财富','财富来源','国家/地区']
    for col in title:
        databox.column(col,width=90,anchor='center')
    i=0
    for colu in column:
        databox.heading(title[i],text=colu)
        i=i+1
    if mtn3==2:
        
        g1=at1.get()
        g2=at2.get()
        if not g1.isdigit() or not g2.isdigit():
            messagebox.showerror(title='错误！！！',message="必须输入有效的数字")
        else:
            g1=int(g1)
            g2=int(g2)
            for row in df1_rows:
                c1=row[2]
                c1=c1[ : -3]
                c1=int(c1)
                if c1 >g1 and c1 < g2:
                    databox.insert('','end',values=row)
    else:
        for row in df1_rows:
            if a=="全部国家" :
                databox.insert('','end',values=row)
            elif row[4]==a:
                databox.insert('','end',values=row)
def no4():
    hh=Toplevel()
    hh.title("统计方式")
    hh.geometry("300x300")
    lb1=tk.Label(hh,text="请选择统计方式",font=('黑体',12),fg='red').place(x=35,y=10)
    but41=tk.Button(hh,text="  各国富豪上榜数 ",cursor='hand2',command=no41).place(x=90,y=55)
    but42=tk.Button(hh,text="各国上榜富豪总财富",cursor='hand2',command=no42).place(x=90,y=155)
    no7(hh)
    mainloop()
    
def no41():
    hh1=Toplevel()
    hh1.title("统计1")
    hh1.geometry("200x400")
    df = pd.read_csv('CCD.csv',encoding='ansi')
    prov = df.groupby('国家/地区')['名字'].count().reset_index(name='数量')
    provi= prov.sort_values(by='数量', ascending=False)
    formatted_output = provi.to_string(index=False, header=True)
    lbh411=tk.Label(hh1,text="各国富豪上榜数量",font=('黑体',11),fg='red').place(x=20,y=10)
    lbh412=tk.Label(hh1,text=formatted_output).place(x=35,y=30)
    no7(hh1)

def no42():
    hh2=Toplevel()
    hh2.title("统计2")
    hh2.geometry("200x400")
    df = pd.read_csv('CCD.csv',encoding='ansi')
    df['财富'] = df['财富'].str.replace('亿美元', '').astype(float)
    wealth_summary = df.groupby('国家/地区')['财富'].sum().reset_index()
    result_string = " "
    for index, row in wealth_summary.iterrows():
        result_string += f"{row['国家/地区']}: {row['财富']:.2f}亿美元\n"
    lbh421=tk.Label(hh2,text="各国富豪财富总量统计",font=('黑体',11),fg='red').place(x=20,y=10)
    lbh422=tk.Label(hh2,text=result_string).place(x=35,y=30)
    no7(hh2)

def no5():
    jj=Toplevel()
    jj.title("视图")
    jj.geometry("300x300")
    lb1=tk.Label(jj,text="请选择视图方式",font=('黑体',12),fg='red').place(x=35,y=10)
    but41=tk.Button(jj,text="各个国家富豪财富总量柱状图",cursor='hand2',command=no51).place(x=90,y=45)
    but42=tk.Button(jj,text="各国富豪财富总量扇形对比图",cursor='hand2',command=no52).place(x=90,y=105)
    but43=tk.Button(jj,text="展示财富来源词云分析",cursor='hand2',command=no53).place(x=90,y=165)
    but45=tk.Button(jj,text="国家上榜次数折线图",cursor='hand2',command=no55).place(x=90,y=215)
    no7(jj)
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
    
def no53():
    df = pd.read_csv('CCD.csv',encoding='ansi')  

    text = ' '.join(df['财富来源'].dropna().astype(str)) 
    seg_list = jieba.cut(text, cut_all=False)
    words = ' '.join(seg_list)

    wordcloud = WordCloud(font_path='simhei.ttf',background_color='white',width=800,height=600,margin=2).generate(words)
    plt.rcParams['font.sans-serif'] = ['SimHei'] 
    plt.rcParams['axes.unicode_minus'] = False  
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.text(0.5,1.1, '财富来源词云分析', ha='center', fontsize=22, transform=plt.gca().transAxes)
    plt.show()
def no55():
    df = pd.read_csv('CCD.csv', encoding='ansi')
    country_counts = df['国家/地区'].value_counts()
    plt.figure(figsize=(12, 5))
    country_counts.plot(kind='line', title='国家/地区上榜次数折线图')
    plt.rcParams["font.sans-serif"]=["SimHei"]
    plt.rcParams['axes.unicode_minus'] = False 
    plt.xlabel('国家/地区')
    plt.ylabel('上榜次数')
    plt.xticks(range(len(country_counts)), country_counts.index, rotation=0)
    plt.show()


def no6():
    global varr
    fhkk=Toplevel()
    fhkk.title("人物查看")
    fhkk.geometry("300x250")
    df = pd.read_csv('CCD.csv', encoding='ansi')
    mz_list=list(df['名字'])
    varr=tkinter.StringVar()
    xzk2=tkinter.ttk.Combobox(fhkk,textvariable=varr,value=(mz_list))
    xzk2.place(x=50,y=60)
    xzk2.current(0)
    varLabel2=tkinter.StringVar()
    
    lb61=tk.Label(fhkk,text="请输入或选择人物以查看",font=('黑体',12),fg='red').place(x=35,y=20)

    butt63 =tk.Button(fhkk,text='显示人物介绍',cursor='hand2',command=cse12).place(x=53,y=90)
    no7(fhkk)

def no7(window):   
    screen_width = window.winfo_screenwidth()  
    screen_height = window.winfo_screenheight()  
    window_width = window.winfo_reqwidth()  
    window_height = window.winfo_reqheight()  
    x = int((screen_width - window_width) / 2)  
    y = int((screen_height - window_height) / 2)   
    window.geometry(f"+{x}+{y}")

def cse1():
    if mtn==2 or mtn==1:
        messagebox.showwarning(title='警告:',message="操 作 重 复!")
    else:
        no1()
        if mtn3==1:
            chae()

                                                                              
def cse2():
    if mtn==2:
        messagebox.showwarning(title='警告:',message="操 作 重 复!")
        
    elif mtn==0:
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
def cse6():
    if mtn==0:
        messagebox.showwarning(title='警告:',message="请先获取数据！")
    else:
        if mtn3==1:
            chea()
        else:
            cheab()
            chae()
def cse7():
    gy=Toplevel()
    gy.title("此系统:")
    gy.geometry("450x300")
    labb71=tk.Label(gy,text="作品名称:  福布斯全球富豪榜实时数据分析系统",font=('黑体',15),fg='blue').place(x=9,y=10)
    labb71=tk.Label(gy,text="制作人员： 席好东,潘骏,余妍.",font=('黑体',15),fg='blue').place(x=9,y=50)
    labb72=tk.Label(gy,text="专业班级： 工商管理 2302班 ",font=('黑体',15),fg='blue').place(x=9,y=90)
    labb73=tk.Label(gy,text="指导教师： 孙占锋 ",font=('黑体',15),fg='blue').place(x=9,y=130)
    butt74=tk.Button(gy, text="打开原网页",cursor='hand2', command=cse9).place(x=59,y=240)
    butt75=tk.Label(gy, text="更多:").place(x=9,y=240)
    butt76=tk.Button(gy,width=0,cursor='hand2', command=cse16).place(x=309,y=5000)
    butt77=tk.Button(gy, text="赞赏",cursor='hand2', command=cse8).place(x=159,y=240)
    butt78=tk.Button(gy, text="投诉",cursor='hand2', command=cse14).place(x=239,y=240)
    butt79=tk.Button(gy, text="致电",cursor='hand2', command=cse13).place(x=199,y=240)
    status_frame = tk.Frame(gy, height=2, bd=1, relief=tk.SUNKEN)  
    status_frame.pack(side=tk.BOTTOM, fill=tk.X)
    statusbar = tk.Label(status_frame, text="郑州轻工业大学 2024/06/19                    感谢支持", anchor=tk.W)   
    statusbar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    no7(gy)
    mainloop()

def cse8():
    url = "https://gongyi.qq.com/succor/project_list.htm"
    webbrowser.open(url, new=2, autoraise=True)
def cse9():
    url = "https://www.phb123.com/renwu/fuhao/shishi.html"
    webbrowser.open(url, new=2, autoraise=True)
def cse13():
    url = "https://mhaoma.baidu.com/pages/search-page/search-page?srcid=10685&query=17364686746"
    webbrowser.open(url, new=2, autoraise=True)
def cse14():
    url = "https://github.com/MaxteinXHH/python-2024.6/issues/1"
    webbrowser.open(url, new=2, autoraise=True)
def cse11():
    if mtn==0:
        messagebox.showwarning(title='警告:',message="请先获取数据！")
    else:
        no6()

def cse12():
    ass=varr.get()
    ass=str(ass)
    url = "https://baike.baidu.com/item/"+ass
    webbrowser.open(url, new=2, autoraise=True)


def cse16():
    messagebox.showwarning(title='提示:',message="ok")
    mtn3=1
    mtn=0
    mtn2=1 

        
root=tk.Tk()
root.title('综合系统')
root.geometry("600x600")
Frame(root, width=120, height=400,bg='pink',padx=100, pady=10).place(x=5,y=90)
Frame(root, width=400, height=350, bg='lightblue').place(x=145,y=85)

button20 =tk.Button(root, text="获取并保存数据",width=12,cursor='hand2', command=cse1).place(x=15,y=100)
labb24=tk.Label(root,text="控 制 台").place(x=35,y=65)
batt06=tk.Button(root,text="处理并保存数据",width=12,cursor='hand2',command=cse2).place(x=15,y=170)
batt18=tk.Label(root,text="福布斯全球富豪榜实时数据分析系统",font=('黑体',22),fg='blue').place(x=49,y=20)
buttonA=tk.Button(root, text="关于",cursor='hand2', command=cse7).place(x=15,y=450)
jjj3 =tk.Button(root,text='    显示排行信息    ',cursor='hand2',command=cse3).place(x=250,y=470)
sss4 =tk.Button(root,text="数据分析与统计",width=12,cursor='hand2',command=cse4).place(x=15,y=240)
zzz4 =tk.Button(root,text="   数据可视化  ",width=12,cursor='hand2',command=cse5).place(x=15,y=310)
yyy6 =tk.Button(root,text='~',cursor='exchange',command=cse6).place(x=368,y=487,width=11,height=11)
zzz5 =tk.Button(root,text=" 查看人物信息 ",width=12,cursor='hand2',command=cse11).place(x=15,y=380)





gj_list=[]
gj_list.append("请先获取数据")
var=tkinter.StringVar()
xzk=tkinter.ttk.Combobox(root,textvariable=var,value=(gj_list))
xzk.place(x=250,y=450)
xzk.current(0)
varLabel=tkinter.StringVar()

def chae():
    global mtn3
    mtn3=1
    df = pd.read_csv('CCD.csv', encoding='ansi')
    gj_set=set(df['国家/地区'])
    gj_list=[]
    gj_list.append("全部国家")
    gj_list.extend(list(gj_set))
    
    xzk=tkinter.ttk.Combobox(root,textvariable=var,value=(gj_list))
    xzk.place(x=250,y=450)
    xzk.current(0)
    varLabel=tkinter.StringVar()
    
def chea():
    global mtn3,at1,at2,ca7,ca8,g1,g2
    mtn3=2
    at1=Entry(root,bd=5,width=6)
    at1.place(x=250,y=445)
    ca7=tk.Label(root,text="————")
    ca7.place(x=300,y=449)
    ca8=tk.Label(root,text="亿美元")
    ca8.place(x=420,y=449)
    at2=Entry(root,bd=5,width=8)
    at2.place(x=350,y=445)

def cheab():
    at1.destroy()
    at2.destroy()
    ca7.destroy()
    ca8.destroy()
       



title=['1','2','3','4','5']
databox=ttk.Treeview(root,columns=title,show='headings')
databox.place(x=150,y=90,width=390,height=340)



can2=tk.Label(root,text="就绪....",font=('黑体',15),bg='white')
can2.place(x=155,y=95)
status_frame = tk.Frame(root, height=20, bd=1, relief=tk.SUNKEN)  
status_frame.pack(side=tk.BOTTOM, fill=tk.X)
statusbar = tk.Label(status_frame, text="就绪", anchor=tk.W)   
statusbar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

root.mainloop()




