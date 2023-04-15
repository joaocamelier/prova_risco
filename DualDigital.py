import numpy as np

def dual_digital(spot1, spot2, barreira1, barreira2, vol1, vol2, corr, t, taxa_livre_risco, n_simulacoes):
    dt = 1 / 252  # 1 dia de trade no ano
    nudt = (taxa_livre_risco - 0.5 * vol1 ** 2 - 0.5 * vol2 ** 2) * dt
    sigmadt1 = vol1 * np.sqrt(dt)
    sigmadt2 = vol2 * np.sqrt(dt)
    lnS1 = np.log(spot1)
    lnS2 = np.log(spot2)
    soma_payoff = 0
    for i in range(n_simulacoes):
        lnSt1 = lnS1 + nudt + sigmadt1 * np.random.normal()
        lnSt2 = lnS2 + nudt + sigmadt2 * (corr * np.random.normal() + np.sqrt(1 - corr** 2) * np.random.normal())
        St1 = np.exp(lnSt1)
        St2 = np.exp(lnSt2)
        if St1 >= barreira1 and St2 >= barreira2:
            soma_payoff += 1
    preco_opcao = np.exp(-taxa_livre_risco * t) * (soma_payoff / n_simulacoes)
    return preco_opcao


