import numpy as np
from scipy.stats import norm

def black_scholes(tipo, s, k, t, r, sigma):
    
    d1 = (np.log(s / k) + (r + sigma ** 2 / 2) * t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    if tipo == 'call':
        preco = s * norm.cdf(d1 , 0 , 1) - k * np.exp(-r * t) * norm.cdf(d2 , 0 , 1)
    elif tipo == 'put':
        preco = k * np.exp(-r * t) * norm.cdf(-d2 , 0 , 1) - s * norm.cdf(-d1 , 0 , 1)
    else:
        print('Parâmetros incorretos.')
    return preco

preco_call = round(black_scholes('call', 100, 110, 1, 0.05, 0.2) , 2)
preco_put = round(black_scholes('put', 100, 110, 1, 0.05, 0.2) , 2)

print(f"Preço da call é: {preco_call}")
print(f"Preço da put é: {preco_put}")