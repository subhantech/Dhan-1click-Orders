# Libraries
import requests
import json
import math

# Python program to print
# colored text and background

# Method to get nearest strikes
def round_nearest(x,num=50): return int(math.floor(float(x)/num)*num)
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
            bnf_nearest=nearest_strike_bnf(bnf_ul)
            nf_nearest=nearest_strike_nf(nf_ul)
            fnf_nearest=nearest_strike_fnf(fnf_ul)
            bnce_itm=nearest_strike_bnf(bnf_ul-100)
            bnpe_itm=nearest_strike_bnf(bnf_ul+100)
            nce_itm=nearest_strike_nf(nf_ul-100)
            npe_itm=nearest_strike_nf(nf_ul+100)
            fnce_itm=nearest_strike_fnf(fnf_ul-100)
            fnpe_itm=nearest_strike_fnf(fnf_ul+100)

            def indiceLTP(self,indice):
                if indice == "nifty":
                    return nf_ul
                if indice == "banknifty":
                    return bnf_ul
                if indice == "finnifty":
                    return fnf_ul
                
            #print(f"samienifty : {indiceLTP('finnifty')}")
            # indiceLTP("banknifty")
            # indiceLTP("finnifty")   


        # # Showing Header in structured format with Last Price and Nearest Strike

        # def print_header(index="",ul=0,nearest=0):
        #     print(strPurple( index.ljust(12," ") + " => ")+ strLightPurple(" Last Price: ") + strBold(str(ul)) + strLightPurple(" Nearest Strike: ") + strBold(str(nearest)))

        # def print_hr():
        #     print(strYellow("|".rjust(70,"-")))



        ################## Added by me to get the Option data #######################

        # print(f"Nifty ITM CE, ITM PE are {nce_itm},{npe_itm}")
        # print(f"Bank Nifty ITM CE, ITM PE are {bnce_itm},{bnpe_itm}")
        # print(f"Fin Nifty ITM CE, ITM PE are {fnce_itm},{fnpe_itm}")


            def put_to_buy(self,indice):
                    if indice == "nifty": 
                        return getOptionStrikes.npe_itm
                    if indice == "finnifty": 
                        return getOptionStrikes.fnpe_itm
                    if indice == "banknifty": 
                        return getOptionStrikes.bnpe_itm

            def call_to_buy(self,indice):
                    if indice == "nifty": 
                        return getOptionStrikes.nce_itm
                    if indice == "finnifty": 
                        return getOptionStrikes.fnce_itm
                    if indice == "banknifty": 
                        return getOptionStrikes.bnce_itm

            #print(call_to_buy("nifty"))
