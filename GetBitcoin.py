import requests
from datetime import datetime

import pandas as pd


#Colocando dentrou de uma função:
def get_bitcoin_df():
    #URL para obter o preco do Bitcoin
    url = "https://api.coinbase.com/v2/prices/spot"

    #criando instância. Requisição GET para a API
    response = requests.get(url)
    data = response.json()

    #Extrair os dados que eu quero
    preco = float(data['data']['amount'])
    ativo = data['data']['base']
    moeda = data['data']['currency']
    horario_de_coleta = datetime.now()

    df = pd.DataFrame([{
        'ativo': ativo, 
        'moeda': moeda,
        'preco': preco,
        'horario_de_coleta': horario_de_coleta
    }])
    
    return df

#print(df)
#Se quiser salvas em csv
#df.to_csv('preco_bitcoin.csv', mode='a', header=False, index=False)

