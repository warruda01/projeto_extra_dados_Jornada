import yfinance as yf #pandas e requests já estão importados
from datetime import datetime 

#jogando tudo para dentro de uma função
def get_commodities_df():
    #ticker é o símbolo do ativo na bolsa
    ultimo_df = yf.Ticker("GC=F").history(period='1d', interval='1m')[['Close']].tail(1)
    ultimo_df = ultimo_df.rename(columns={'Close': 'preco'})
    ultimo_df['ativo'] = 'GC=F'
    ultimo_df['moeda'] = 'USD'
    ultimo_df['horario_coleta'] = datetime.now()
    ultimo_df = ultimo_df[['ativo', 'preco', 'moeda', 'horario_coleta']]


    return ultimo_df
#Se quiser mostrar todas as colunas:
#pd.set_option('display.max_columns', None)

#print(df.tail()) #Sequiser pegar todos os valores
 