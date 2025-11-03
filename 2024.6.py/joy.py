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


 


def no4():
    hh=Toplevel()
    hh.title("统计方式")
    hh.geometry("300x300")
    lb1=tk.Label(hh,text="请选择统计方式",fg='red').place(x=35,y=10)
    but41=tk.Button(hh,text="统计各省高校数量").place(x=90,y=55)
    but42=tk.Button(hh,text="统计各类型各省数量").place(x=90,y=155)
    mainloop()
           
root=tk.Tk()
root.title('综合实验')
root.geometry("400x400")


Frame(root, width=120, height=400, bg='pink',padx=100, pady=10).place(x=105,y=85)
what =tk.Button(root, text="获取并保存数据",command=no4).place(x=115,y=95)
can  =tk.Label(root,text="控 制 台").place(x=135,y=60)
I    =tk.Button(root,text="处理并保存数据").place(x=115,y=155)
say  =tk.Label(root,text="中国民办高校数据统计与可视化",font=('黑体',15),fg='blue').place(x=39,y=20)

but3 =tk.Button(root,text='显示学校信息',).place(x=150,y=450)
but4 =tk.Button(root,text="   数据统计    ").place(x=115,y=215)
but4 =tk.Button(root,text="   数据可视化    ").place(x=115,y=275)

status_frame = tk.Frame(root, height=20, bd=1, relief=tk.SUNKEN)  
status_frame.pack(side=tk.BOTTOM, fill=tk.X)
statusbar = tk.Label(status_frame, text="就绪", anchor=tk.W)   
statusbar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
 

root.mainloop()
