import yfinance as yf
import numpy as np
import pandas as pd
import warnings
import plots
warnings.filterwarnings("ignore", message=".*inplace keyword.*")

us_obligations = yf.download('^IRX', progress=False)['Close'].squeeze().iloc[-1]/100
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META', 'TSLA', 'JPM', 'LLY', 'XOM']
prices = yf.download(stocks, progress=False, start='2020-01-01')['Close']

returns = np.log(prices / prices.shift(1)).dropna()
mean_returns = returns.mean()*252
cov_matrix = returns.cov()*252

pr_list=[]
pvol_list=[]
sharpe_list=[]
weights_list=[]

for i in range(10000):
    weights=np.random.random(len(stocks))
    weights/=np.sum(weights)
    portfolio_return = np.sum(mean_returns * weights)
    portfolio_volatility = np.sqrt(weights @ cov_matrix @ weights)
    sharpe_ratio=(portfolio_return-us_obligations)/portfolio_volatility
    pr_list.append(portfolio_return)
    pvol_list.append(portfolio_volatility)
    sharpe_list.append(sharpe_ratio)
    weights_list.append(weights)

argmax_sharpe = np.argmax(sharpe_list)
max_sharpe_ret = pr_list[argmax_sharpe]
max_sharpe_vol = pvol_list[argmax_sharpe]
max_sharpe_w = pd.Series(weights_list[argmax_sharpe], index=returns.columns)

argmin_vol = np.argmin(pvol_list)
min_vol_ret = pr_list[argmin_vol]
min_vol_vol = pvol_list[argmin_vol]
min_vol_w = pd.Series(weights_list[argmin_vol], index=returns.columns)

print(f"Max Sharpe Portfolio (Sharpe: {sharpe_list[argmax_sharpe]:.2f})")
print(f"Annual Return: {max_sharpe_ret:.2%} | Annual Volatility: {max_sharpe_vol:.2%}")
print(max_sharpe_w.round(4))

print(f"\nMin Volatility Portfolio")
print(f"Annual Return: {min_vol_ret:.2%} | Annual Volatility: {min_vol_vol:.2%}")
print(min_vol_w.round(4))

plots.plot_frontier(pvol_list, pr_list, sharpe_list, max_sharpe_vol, max_sharpe_ret, min_vol_vol, min_vol_ret)