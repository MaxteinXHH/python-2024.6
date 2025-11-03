name="maxcomp"
now_stock_price =590

stock_code =105499
stock_price_daily_growth_factor=1.2
a=int(input("days"))
stock_price =now_stock_price*(1.2**a)
stock_price =round(stock_price,4)
print(f"公司：{name},股票代码：{stock_code}当日股价：{now_stock_price}。")
print("\n 每日增长系数为：%d,经过 %d 天的增长后，股价达到了 %d " %(stock_price_daily_growth_factor, a ,stock_price))

