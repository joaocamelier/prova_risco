import yfinance as yf
import pandas as pd

tickers = [ 'SPY' , 'GLD' , 'XLY' , 'XLF' , 'XLE']

# aaaa-mm-dd
data_inicio = '2012-01-02'
data_final = '2022-10-17'

def dados_tickers( tickers , data_inicio, data_final ):
  df = pd.DataFrame()
  for i in tickers:
    df[i] =  yf.download( tickers = i , start= data_inicio , end= data_final)['Adj Close']
    df = df.ffill()
  return df

df =  dados_tickers( tickers , data_inicio, data_final )
df = df.rename({'^GSPC': 'S&P500'}, axis = 1)
df = df.rename({'^BVSP': 'IBOVESPA'}, axis = 1)

def beta(df , benchmark): # para Ibovespa = ^BVSP

    df[f'{benchmark}'] = yf.download(tickers = f'{benchmark}' , start = data_inicio , end = data_final)['Adj Close']
    Tabela = pd.DataFrame()

    for ativo in tickers:
        retornos_df = df.pct_change()
        cov = retornos_df.cov().loc[ativo , f'{benchmark}']
        
        retornos_bench = df[f'{benchmark}'].pct_change()
        var = retornos_bench.var()

        beta = cov / var

        Tabela.loc[ativo , f'Em relação a {benchmark}'] = beta
    
    df.drop(columns = f'{benchmark}' , inplace = True) 
    
    if benchmark == '^GSPC':
        Tabela = Tabela.rename({'Em relação a ^BVSP': 'Em relação a IBOVESPA'}, axis = 1)

    else:
        pass

    
    return Tabela

beta(df , 'SPY')
