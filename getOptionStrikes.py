# Libraries
import requests
import json
import math
import schedule
import time


# Method to get nearest strikes
# def round_nearest(x,num=50): return int(math.floor(float(x)/num)*num)
def round_nearest(x,num=100): 
     if x % num > 50 :
        return int(math.ceil(float(x)/num)*num)
     if x % num <= 50 :
        return int(math.floor(float(x)/num)*num)
def nearest_strike_bnf(x): return round_nearest(x,100)
def nearest_strike_nf(x): return round_nearest(x,100)
def nearest_strike_fnf(x): return round_nearest(x,100)

# Urls for fetching Data
url_oc      = "https://www.nseindia.com/option-chain"
url_bnf     = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'
url_nf      = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
url_fnf     = 'https://www.nseindia.com/api/option-chain-indices?symbol=FINNIFTY'
url_indices = "https://www.nseindia.com/api/allIndices"

# Headers
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'accept-language': 'en,gu;q=0.9,hi;q=0.8',
            'accept-encoding': 'gzip, deflate, br'}

sess = requests.Session()
cookies = dict()

# Local methods
def set_cookie():
    request = sess.get(url_oc, headers=headers, timeout=5)
    cookies = dict(request.cookies)

def get_data(url):
    set_cookie()
    response = sess.get(url, headers=headers, timeout=5, cookies=cookies)
    if(response.status_code==401):
        set_cookie()
        response = sess.get(url_nf, headers=headers, timeout=5, cookies=cookies)
    if(response.status_code==200):
        return response.text
    return ""

class   getOptionStrikes:
            global indice
            global bnf_ul
            global nf_ul
            global fnf_ul
            global bnf_nearest
            global nf_nearest
            global fnf_nearest
            global bnce_itm
            global bnpe_itm
            global nce_itm
            global npe_itm
            global fnce_itm
            global fnpe_itm
            response_text = get_data(url_indices)
            data = json.loads(response_text)
            for index in data["data"]:
                if index["index"]=="NIFTY 50":
                    nf_ul = index["last"]
                    print(f"nifty LTP {nf_ul}")
                if index["index"]=="NIFTY BANK":
                    bnf_ul = index["last"]
                    print(f"banknifty LTP {bnf_ul}")
                if index["index"]=="NIFTY FINANCIAL SERVICES":
                    fnf_ul = index["last"]
                    print(f"finnifty LTP {fnf_ul}")

            def indiceLTP(self,indice):
                if indice == "nifty":
                    nce_itm=nearest_strike_nf(nf_ul-100)
                    npe_itm=nearest_strike_nf(nf_ul+100)

                    return {"niftyltp" :nf_ul, "niftyitmcall": nce_itm, "niftyitmput": npe_itm}
                
                if indice == "banknifty":
                    bnce_itm=nearest_strike_bnf(bnf_ul-100)
                    bnpe_itm=nearest_strike_bnf(bnf_ul+100)

                    return {"bankniftyltp" : bnf_ul, "bankniftyitmcall" :bnce_itm, "bankniftyitmput": bnpe_itm}
                
                if indice == "finnifty":
                    fnce_itm=nearest_strike_fnf(fnf_ul-100)
                    fnpe_itm=nearest_strike_fnf(fnf_ul+100)

                    return {"finniftyltp" : fnf_ul, "finniftyitmcall" : fnce_itm, "finniftyitmput" : fnpe_itm } 
                
