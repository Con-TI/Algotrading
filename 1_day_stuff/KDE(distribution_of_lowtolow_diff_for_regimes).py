import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

data = pd.read_pickle('../Data_Collection/clean_data_1day.pkl')
filtered_data = pd.read_pickle('../Data_Collection/clean_data_1day.pkl')
# filtered_data = filtered_data[-300:]

list_of_flat_stocks = []
for column in filtered_data['Close'].columns:
    current_series = filtered_data['Close'][column]
    if has_consecutive_repeats(current_series, 30):
        list_of_flat_stocks.append(column)

stock_codes = [column for column in filtered_data['Close'].columns if column not in list_of_flat_stocks]

def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False  # Number is divisible by divisor, so it's not prime
    return True

def find_factor_pair(number):
    if is_prime(number):
        number = number+1
    factor_pairs = []
    sqrt_num = math.isqrt(number)
    for i in range(1, int(math.ceil(sqrt_num + 1))):
        if number % i == 0:
            factor_pairs.append((int(i), int(number / i)))
    diff = 100
    optimal_pair = ()
    for pair in factor_pairs:
        if abs(pair[1]-pair[0]) < diff:
            diff = abs(pair[1]-pair[0])
            optimal_pair = pair
    return optimal_pair

def concatenate(feature,regime):
    return pd.concat([feature,regime],axis=1,)

for stock in stock_codes:
    close_prices = filtered_data['Close'][stock]
    open_prices = filtered_data['Open'][stock]
    high_prices = filtered_data['High'][stock]
    low_prices = filtered_data['Low'][stock]
    day_change = ((open_prices-open_prices.shift(1))/open_prices.shift(1) * 100)[1:]
    regime = day_change.floordiv(1.5)
    low_to_low_spread = ((low_prices - low_prices.shift(1)) / low_prices.shift(1) * 100)[1:]
    low_to_low_spread = concatenate(low_to_low_spread,regime)
    low_to_low_spread.columns = [stock, 'regime']
    low_spreads_by_regime = [group for _, group in low_to_low_spread.sort_values(by='regime',ascending=True).groupby('regime') if len(group)>=20]
    unique_regimes = [df.iat[0,1] for df in low_spreads_by_regime]
    # figure = plt.figure(figsize=(12,8))
    pair = find_factor_pair(len(unique_regimes))
    # grid = plt.GridSpec(nrows=pair[0],ncols=pair[1])
    figure, axis = plt.subplots(nrows=pair[0],ncols=pair[1],figsize=(12,8),num=stock)
    n=-1
    for regime in unique_regimes:
        n+=1
        column = int(n % pair[1])
        row = int(math.floor(n/pair[1]))
        index = unique_regimes.index(regime)
        spreads = low_spreads_by_regime[index][stock]
        # axis[row,column].plot(spreads.index,spreads.values)
        sns.kdeplot(spreads.values, ax=axis[row,column])
        if regime == 0:
            axis[row,column].set_title(f'Regime:{regime}, -1.5 to 1.5 change')
        elif regime > 0:
            axis[row,column].set_title(f'Regime:{regime}, {regime*1.5} to {(regime+1)*1.5} change')
        elif regime < 0:
            axis[row, column].set_title(f'Regime:{regime}, {(regime-1) * 1.5} to {regime * 1.5} change')
    fig_mgr = plt.get_current_fig_manager()
    fig_mgr.window.wm_geometry("+0+0")
    plt.tight_layout()
    plt.show()