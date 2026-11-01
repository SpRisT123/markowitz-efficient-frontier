import matplotlib.pyplot as plot
import matplotlib.ticker as mtick

def plot_frontier(pvol_list, pr_list, sharpe_list, max_sharpe_vol, max_sharpe_ret, min_vol_vol, min_vol_ret):
    plot.style.use('bmh')
    plot.figure(num='Markowitz Efficient Frontier', figsize=(9, 6))

    plot.scatter(pvol_list, pr_list, c=sharpe_list, cmap='plasma', s=5)
    plot.colorbar(label='Sharpe Ratio')

    plot.scatter(max_sharpe_vol, max_sharpe_ret, color='#6395EE', alpha=1, marker='*', s=170, label=f'Max Sharpe ({max_sharpe_ret:.1%} Return, {max_sharpe_vol:.1%}  Volatility)')
    plot.scatter(min_vol_vol, min_vol_ret, color='#2E6F40', alpha=1, marker='*', s=170, label=f'Min Volatility ({min_vol_ret:.1%} Return, {min_vol_vol:.1%}  Volatility)')

    plot.gca().xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    plot.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    
    plot.title('Markowitz Efficient Frontier', fontsize=16)
    plot.xlabel('Annual Volatility', fontsize=14)
    plot.ylabel('Expected Annual Return', fontsize=14)
    plot.legend(frameon=False, loc='upper left', fontsize=10)
    plot.savefig('charts/efficient_frontier.png', dpi=150)
    plot.show()