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
            try:
                val = data[i]["media"]
            except KeyError:
                continue 
        if val is not None:
            try:
                val = data[i]["media"]["webpage"]
            except KeyError:
                continue 
        if val is not None:
            try:
                val = data[i]['media']['webpage']['description']
            except KeyError:
                continue     
            print(val)
            start = val.find("$")
            end = val[start:].find(" ")
            tckr = val[start:end]
            tickers.append(tckr)
    for i in range(0, len(tickers)):
        ticker = tickers[i]
        if(ticker!="" and ticker !=" "):
            parsed_ticker = ticker[1: len(ticker)]
            parsed_tickers.append(parsed_ticker)
    
    return parsed_tickers
