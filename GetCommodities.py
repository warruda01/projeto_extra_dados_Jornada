import yfinance as yf #pandas e requests já estão importados
from datetime import datetime 
import pandas as pd

#jogando tudo para dentro de uma função
def get_commodities_df():
    symbols = ["GC=F", "CL=F", "SI=F"] #Queremos pegar três variáveis, Ouro, Crude, Silver
    #Teremos uma lista de Dataframes. Rodará uma vez em cada um dos acima. Cada vez, 
    # acrescentará as variáveis abaixo na lista
    dfs = []
    for sym in symbols:

    #ticker é o símbolo do ativo na bolsa
        ultimo_df = yf.Ticker("GC=F").history(period='1d', interval='1m')[['Close']].tail(1)
        ultimo_df = ultimo_df.rename(columns={'Close': 'preco'})
        ultimo_df['ativo'] = sym
        ultimo_df['moeda'] = 'USD'
        ultimo_df['horario_coleta'] = datetime.now()
        ultimo_df = ultimo_df[['ativo', 'preco', 'moeda', 'horario_coleta']]
        dfs.append(ultimo_df)
    #Após fazer por três vezes vai concatenar dentrou de um MEtaframe
    return pd.concat(dfs, ignore_index=True)

    return ultimo_df
#Se quiser mostrar todas as colunas:
#pd.set_option('display.max_columns', None)

#print(df.tail()) #Sequiser pegar todos os valores
 