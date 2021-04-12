import requests

def get_price(ticker):
    r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={ticker}&token=c1nvk2i37fkv6lmc7hmg')
    
    """
    o opening
    h high of day
    l low of day
    c current price
    pc previous close
    """

    return r.json()["c"]
