import tkinter as tk  
from tkinter import filedialog  
import pandas as pd  
import plotly.express as px  
  
def no51():  
    root = tk.Tk()  
    root.withdraw()  
    file_path = filedialog.askopenfilename(filetypes=[("CCD.csv", "*.csv")])  # 修正文件类型过滤器  
    if file_path:  # 确保用户选择了文件  
        df = pd.read_csv(file_path, dtype={'国家/地区': str})  # 读取CSV文件  
  
        # 绘制柱状图  
        fig_bar = px.bar(df, x='国家/地区', y='某个计数列')  # 假设您想根据某个计数列来绘制  
        fig_bar.update_layout(title='各国家进入500强企业数量', xaxis_title='国家/地区', yaxis_title='数量')  
        fig_bar.show()  
  
        # 绘制饼图  
        sector_counts = df["主要赛道"].value_counts()  
        fig_pie = px.pie(values=sector_counts.values, names=sector_counts.index, title='各赛道进入500强的数量')  
        fig_pie.show()  
  
# 注意这里没有再次定义函数，只是上面的函数定义
no51()
