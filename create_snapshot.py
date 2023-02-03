
import yfinance as yf
import pandas as pd
import json
import matplotlib.pyplot as plt

def webreq_df():
    s = json.load(open("jenny_portfolio.json", 'r'))
    reformatted = {}
    
    for s_dict in s["stocks"]:
        reformatted[s_dict["ticker"]] = {x: s_dict[x] for x in s_dict if x not in {"ticker"}}

    print("Stock information read...")

    ticks = "".join([x + " " for x in reformatted.keys()])

    historical_data = yf.download(
        tickers = ticks,
        period = '3mo', # valid periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
        interval = '1d',
        group_by = 'ticker',
    )

    historical_data.to_csv("Past_data.csv")
    
def df_analyze():

    df = pd.read_csv("Past_data.csv")

    # duplicate shit. shush
    s = json.load(open("jenny_portfolio.json", 'r'))
    reformatted = {}
    
    for s_dict in s["stocks"]:
        reformatted[s_dict["ticker"]] = {x: s_dict[x] for x in s_dict if x not in {"ticker"}}
    #

    past_closes = []
    past_keys = []
    dates = pd.to_datetime(df['dates'][2:])
    
    for ticker in reformatted.keys():
        past_keys.append(ticker)
        z = pd.to_numeric(df[ticker + ".4"][2:])
        # z = [int(round(float(i))) for i in z]
        # print(z)
        plt.plot(dates, z)
        past_closes.append(z)

    plt.tick_params(axis="x", labelrotation=60)
    plt.tight_layout()
    plt.savefig("Composition Graph.png")
    plt.stackplot(dates, past_closes)
    plt.tick_params(axis="x", labelrotation=60)
    plt.tight_layout()
    plt.savefig("Stackplot.png")
    

if __name__ == "__main__":
    #webreq_df()
    df_analyze()