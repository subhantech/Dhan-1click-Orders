from pandas import pandas as pd
pddf = pd.read_csv('api-scrip-master.csv')

expiry = "2023-06-27"
indice = "FINNIFTY "
expiry_day = "11 "
expiry_month = "JUL "
strikeprice = "20200 "
option_type = "CALL"

newdf = pddf[pddf['SEM_CUSTOM_SYMBOL'].str.contains(strikeprice) & pddf['SEM_TRADING_SYMBOL'].str.contains(indice) & pddf['SEM_INSTRUMENT_NAME'].str.contains("OPTIDX") & pddf['SEM_EXPIRY_DATE'].str.contains(expiry) & pddf['SEM_CUSTOM_SYMBOL'].str.contains("CALL")]
newdf['SEM_SMST_SECURITY_ID']

option_to_buy = indice + expiry_day + expiry_month + strikeprice + option_type
#print(option_to_buy)


#this code will get option security id to order
optionpddf = pddf[pddf['SEM_CUSTOM_SYMBOL'] == option_to_buy ]
#print(optionpddf)
buy_call_id = optionpddf['SEM_SMST_SECURITY_ID'].loc[optionpddf.index[0]]
print(buy_call_id)
