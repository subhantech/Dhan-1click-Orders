import polars as plrs
import polars.selectors as cs
import getOptionStrikes
from datetime import datetime,date
import getExpiryDays

pddf = plrs.read_csv("api-scrip-master.csv")


#expiry = "2023-06-27"
expiry = getExpiryDays.nextTuesday
indice = "FINNIFTY "
expiry_day = "11 "
expiry_month = "JUL "
strikeprice = "20200 "
option_type = "CALL"

option_to_buy = indice + expiry_day + expiry_month + strikeprice + option_type

pddf_data = pddf.filter(plrs.col("SEM_CUSTOM_SYMBOL") == option_to_buy )
pddf_sid = pddf_data.select(plrs.col("SEM_SMST_SECURITY_ID")).item(0,0)
print(pddf_sid)

