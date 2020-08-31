import time 
from libs.openexchange import OpenExchangeClient

APP_ID = "a47c10229d3c4b769b300ec29deaeb51"
client = OpenExchangeClient(APP_ID)

usd_amount = 1000

start = time.time()
gbp_amount = client.convert(usd_amount,"USD","GBP")
end = time.time()



print(end - start)
print(end - start)

print(f"USD{usd_amount} is GBP{gbp_amount:.2f}")   