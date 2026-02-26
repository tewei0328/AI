import pandas as pd
import matplotlib.pyplot as plt

# 備註：在 Google Colab 中，您可以先執行以下指令安裝 yfinance：
# !pip install yfinance

# 試著使用 yfinance 抓取台積電 (2330.TW) 的股價資料
try:
    import yfinance as yf

    # 設定股票代碼，台積電在台股的代碼是 2330.TW
    ticker = "2330.TW"

    # 下載最近一年的資料
    df = yf.download(ticker, period="1y")

    # 畫出收盤價走勢圖
    plt.figure(figsize=(10, 6))
    df['Close'].plot()
    plt.title('TSMC (2330.TW) Stock Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Price (TWD)')
    plt.grid(True)
    plt.show()

except ImportError:
    print("請先安裝 yfinance 套件：!pip install yfinance")
except Exception as e:
    print(f"發生錯誤：{e}")
