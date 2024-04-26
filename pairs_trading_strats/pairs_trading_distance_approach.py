import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from itertools import combinations
from matplotlib.backends.backend_pdf import PdfPages

filtered_data = pd.read_pickle('../Data_Collection/clean_data_1day.pkl')
# Clean data contains 5minute price data for the stocks in stock_codes
close_prices = filtered_data['Close']
percentage_changes_1step = close_prices.pct_change(periods=1)

pp = PdfPages('../pdfs/pairs_trading/pairs_distance.pdf')

# 3.TODO organising data (remove stocks that don't move much and stocks with long flat portions)
def has_consecutive_repeats(column, num_of_repeat):
    prev_value = None
    consecutive_count = 1
    for value in column:
        if value == prev_value:
            consecutive_count += 1
            if consecutive_count > num_of_repeat:
                return True
        else:
            consecutive_count = 1
        prev_value = value
    return False


list_of_flat_stocks = []
for column in close_prices.columns:
    current_series = close_prices[column]
    if has_consecutive_repeats(current_series, 70):
        list_of_flat_stocks.append(column)
# print(len(list_of_flat_stocks))
percentage_changes_1step = percentage_changes_1step.drop(columns=list_of_flat_stocks)

pairs = list(combinations([stock for stock in list(close_prices.columns) if stock not in list_of_flat_stocks],2))

# 4.TODO Plotting pairs without lag
distances_for_pairs = []
for pair in pairs:
    series1 = close_prices[pair[0]].reset_index(drop=True)
    series2 = close_prices[pair[1]].reset_index(drop=True)
    distance_squared = np.sum((series1-series2)**2)
    distances_for_pairs.append(distance_squared)
temp = pd.DataFrame({'pairs':pairs,'dist':distances_for_pairs})
temp = temp.sort_values(by='dist',ascending=True)
considered = temp[:100]
for pair in considered['pairs'].to_list():
    series1 = close_prices[pair[0]].reset_index(drop=True)
    series2 = close_prices[pair[1]].reset_index(drop=True)
    figure = plt.figure(figsize=(10,6),)
    grid = plt.GridSpec(nrows=3,ncols=1)
    ax1 = figure.add_subplot(grid[0,0])
    ax1.plot(series1.index, series1.values,color='b')
    ax2 = ax1.twinx()
    ax2.plot(series2.index, series2.values, color='r')
    ax1.set_xlabel('time')
    ax1.set_ylabel(f'price {pair[0]}')
    ax2.set_ylabel(f'price {pair[1]}')
    ax1.set_title(f'Blue: {pair[0]}, Red: {pair[1]}')
    ax3 = figure.add_subplot(grid[1,0],sharex=ax1)
    normalized1 = (series1-series1.min())/(series1.max()-series1.min())
    normalized2 = (series2-series2.min())/(series2.max()-series2.min())
    ax3.plot(normalized1.index,normalized1.values,color='b')
    ax3.plot(normalized2.index,normalized2.values,color='r')
    ax3.set_xlabel('time')
    ax3.set_ylabel('normalized prices')
    ax4 = figure.add_subplot(grid[2,0],sharex=ax1)
    spread = normalized1-normalized2
    ax4.plot(spread)
    ax4.set_xlabel('time')
    ax4.set_ylabel('spread series')
    ax4.axhline(spread.mean(),color='k',linestyle='--')
    ax4.axhline(spread.mean()+spread.std(),color='r',linestyle='--')
    ax4.axhline(spread.mean()-spread.std(),color='g',linestyle='--')
    ax4.set_title(f'Green: Buy {pair[0]}, Red: Buy {pair[1]}')
    plt.tight_layout()
    pp.savefig()
    plt.close()
    # plt.show()
pp.close()