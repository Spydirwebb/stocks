import json
import re

def parse_data():   
    tickers = []
    parsed_tickers = []
    pattern = "$\|(.*?)|\s"
    f = open('channel_messages.json',)
    data = json.load(f)

    for i in range(0, len(data)):
        val = data[i]
        if val is not None:
            val = data[i]["media"]
        if val is not None:
            val = data[i]["media"]["webpage"]
        if val is not None:
            val = data[i]['media']['webpage']['description']
            print(val)
            start = val.find("$")
            end = val[start:].find(" ")
            tckr = val[start:end]
            tickers.append(tckr)
    print(f"ticker: {tickers}")
    for i in range(0, len(tickers)):
        ticker = tickers[i]
        if(ticker!=""):
            parsed_ticker = ticker[1: len(ticker)]
            parsed_tickers.append(parsed_ticker)
    
    return parsed_tickers
