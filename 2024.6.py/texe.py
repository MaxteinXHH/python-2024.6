import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('CCD.csv', encoding='ansi') 

province_counts = df['省市'].value_counts().reset_index()
province_counts.columns = ['省市', '高校数量']

plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False  
fig, ax = plt.subplots(figsize=(10, 6)) 
bars = ax.bar(province_counts['省市'], province_counts['高校数量'], color='skyblue')

def add_numbers(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_numbers(bars)

ax.set_title('各省高校数量')
ax.set_xlabel('省市')
ax.set_ylabel('高校数量')

ax.set_xticklabels(province_counts['省市'], rotation=45, ha='right')

plt.tight_layout() 
plt.show()
