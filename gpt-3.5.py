from openai import OpenAI

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
import time
import tkinter.ttk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
from tkinter.messagebox import *
import webbrowser
from PIL import Image, ImageTk

model="gpt-3.5-turbo"

print("欢迎。。。。。")

def ai2():

    ques=entry132.get("1.0", tk.END)
    custom_print("\n")
    custom_print("\n")
    custom_print("\n")

    custom_print("您：")
    custom_print("\n")
    custom_print("\n")

    custom_print(ques)

    custom_print("\n")
    custom_print("GPT :")
    custom_print("\n")
    custom_print("\n")


    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        #sk-ATeb0TGZKhyrwsFF5L3iQdN6vF9Rwx3SvyPDHeOOHp1QXI2y
        api_key="sk-bCbCM9wHwvvSRtf82NHZbf9E2af60rIGheV2POQFsVyPoBbM",
        base_url="https://api.chatanywhere.tech/v1"
    )



    # 非流式响应
  

    def gpt_35_api(messages: list):
        """为提供的对话消息创建新的回答

        Args:
            messages (list): 完整的对话消息
        """
        completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        print(completion.choices[0].message.content)

    def gpt_35_api_stream(messages: list):

        """为提供的对话消息创建新的回答 (流式传输)

        Args:
            messages (list): 完整的对话消息
        """
        stream = client.chat.completions.create(model="gpt-3.5-turbo",messages=messages,stream=True,)
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                custom_print(chunk.choices[0].delta.content)

    if __name__ == '__main__':
        messages = [{'role': 'user','content': ques},]
        # 非流式调用
        # gpt_35_api(messages)
    # 流式调用
        gpt_35_api_stream(messages)

roo=tk.Tk()
roo.title('对话系统')
    
roo.geometry("1000x1000")
Frame(roo, width=1000, height=400, bg='pink', padx=100, pady=10).place(x=5, y=460)
sz1 = tk.Label(roo, text="问题:",font=('黑体',13),width=7,bg='cyan')
sz1.place(x=90, y=500)
entry132 = tk.Text(roo, width=80, height=16)
entry132.place(x=200, y=500)

text_widget = tk.Text(roo,height = 30,width =120)
text_widget.pack()
# 定义一个函数来输出文本，而不是使用print
def custom_print(text):
    
 text_widget.insert(tk.END,text)    

    
button808 =tk.Button(roo, text="开始提问",width=12,cursor='hand2', command=ai2).place(x=250,y=760)

custom_print("欢迎。。。。。")


 

can2=tk.Label(roo,text="Chat-gpt-4o-mini",font=('黑体',15),bg='lime')
can2.place(x=200,y=465)
status_frame = tk.Frame(roo, height=20, bd=1, relief=tk.SUNKEN)  
status_frame.pack(side=tk.BOTTOM, fill=tk.X)
statusbar2 = tk.Label(status_frame, text="就绪", anchor=tk.W)   
statusbar2.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    
roo.mainloop()














