import pandas as pd
from GetBitcoin import get_bitcoin_df
from GetCommodities import get_commodities_df
#from GetCommodities import...

valor_bitcoin = get_bitcoin_df()
valor_commodities = get_commodities_df()

print(valor_bitcoin)
print(valor_commodities)