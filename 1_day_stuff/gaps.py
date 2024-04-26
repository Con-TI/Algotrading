import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import itertools
import numpy as np

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
    if has_consecutive_repeats(current_series, 10):
        list_of_flat_stocks.append(column)

stock_codes = [column for column in filtered_data['Close'].columns if column not in list_of_flat_stocks]
filtered_data_close = filtered_data['Close'][stock_codes]
filtered_data_open = filtered_data['Open'][stock_codes]
filtered_data_day_change = 100*(filtered_data_close-filtered_data_open)/filtered_data_open
filtered_data_gaps = 100*(filtered_data_open-filtered_data_close.shift(1))/filtered_data_close.shift(1)
all_conditions_fulfilled_long = ((filtered_data_day_change > 2) & ((filtered_data_gaps.shift(-1).fillna(0) > 3) | (filtered_data_gaps.shift(-1).fillna(0) < -3 ))).sum(axis=1).to_list()
all_conditions_fulfilled_short = ((filtered_data_day_change < -2) & ((filtered_data_gaps.shift(-1).fillna(0) > 3) | (filtered_data_gaps.shift(-1).fillna(0) < -3 ))).sum(axis=1).to_list()
just_gap_down = ((filtered_data_day_change > 2) & (filtered_data_gaps.shift(-1).fillna(0) < -3 )).sum(axis=1).to_list()

above_2_count = (filtered_data_day_change > 2).sum(axis=1).to_list()

threshold = 3
series1 = []
series2 = []
series3 = []
series4 = []
series5 = []
series6 = []
for stock in stock_codes:
    open_prices = filtered_data_open[stock]
    close_prices = filtered_data_close[stock]
    gaps = filtered_data_gaps[stock]
    daily_change = filtered_data_day_change[stock]
    previous_day_change = daily_change.shift(1)
    merged = pd.concat([gaps,daily_change,previous_day_change],axis=1)
    merged.columns = [f'{stock} gap',f'{stock} change',f'{stock} previous change']
    gap_down = merged[merged[f'{stock} gap'] < -threshold]
    gap_up = merged[merged[f'{stock} gap'] > threshold]
    series1.append(gap_down[f'{stock} change'].to_list())
    series2.append(gap_up[f'{stock} change'].to_list())
    series3.append(gap_down[gap_down[f'{stock} previous change']>2][f'{stock} previous change'].to_list())
    series4.append(gap_down[gap_down[f'{stock} previous change']<-2][f'{stock} previous change'].to_list())
    series5.append(gap_up[gap_up[f'{stock} previous change']>2][f'{stock} previous change'].to_list())
    series6.append(gap_up[gap_up[f'{stock} previous change']<-2][f'{stock} previous change'].to_list())
series1 = list(itertools.chain.from_iterable(series1))
series2 = list(itertools.chain.from_iterable(series2))
series3 = list(itertools.chain.from_iterable(series3))
series4 = list(itertools.chain.from_iterable(series4))
series5 = list(itertools.chain.from_iterable(series5))
series6 = list(itertools.chain.from_iterable(series6))

def add_v_lines(axis,series):
    axis.axvline(np.mean(series),linestyle='--',color='k')
    axis.axvline(np.mean(series)+np.std(series),linestyle='--',color='y')
    axis.axvline(np.mean(series)-np.std(series),linestyle='--',color='y')
    axis.axvline(np.mean(series)+2*np.std(series),linestyle='--',color='g')
    axis.axvline(np.mean(series)-2*np.std(series),linestyle='--',color='g')

figure = plt.figure()
grid = plt.GridSpec(nrows=3,ncols=4)
axis1 = figure.add_subplot(grid[0,0])
axis1.set_title(f'Distribution of pct daily change\n on gap down days (-{threshold})')
sns.kdeplot(series1,ax=axis1)
add_v_lines(axis1,series1)

axis12 = figure.add_subplot(grid[1,0])
axis12.set_title('Distribution of pct daily change\n on gap down days\n given previous positive')
sns.kdeplot(series3, ax=axis12)
add_v_lines(axis12,series3)

axis123 = figure.add_subplot(grid[2,0])
axis123.set_title('Distribution of pct daily change\n on gap down days\n given previous negative')
sns.kdeplot(series4, ax=axis123)
add_v_lines(axis123,series4)

axis2 = figure.add_subplot(grid[0,1])
axis2.set_title(f'Distribution of pct daily change\n on gap up days (+{threshold})')
sns.kdeplot(series2,ax=axis2)
add_v_lines(axis2,series2)

axis22 = figure.add_subplot(grid[1,1])
axis22.set_title('Distribution of pct daily change\n on gap down days\n given previous positive')
sns.kdeplot(series5, ax=axis22)
add_v_lines(axis22,series5)

axis223 = figure.add_subplot(grid[2,1])
axis223.set_title('Distribution of pct daily change\n on gap down days\n given previous negative')
sns.kdeplot(series6, ax=axis223)
add_v_lines(axis223,series6)

axis3 = figure.add_subplot(grid[0,2])
sns.kdeplot(above_2_count,ax=axis3)
axis3.set_title('Distribution of stocks per day\n with above 2 pct change')
add_v_lines(axis3,above_2_count)

axis4 = figure.add_subplot(grid[1,2])
sns.kdeplot(all_conditions_fulfilled_long,ax=axis4)
axis4.set_title('Distribution of stocks per day\n which satisfy all cond for long')
add_v_lines(axis4, all_conditions_fulfilled_long)

axis5 = figure.add_subplot(grid[2,2])
sns.kdeplot(all_conditions_fulfilled_long,ax=axis5)
axis5.set_title('Distribution of stocks per day\n which satisfy all cond for short')
add_v_lines(axis5, all_conditions_fulfilled_short)

axis6 = figure.add_subplot(grid[1,3])
sns.kdeplot(just_gap_down,ax=axis6)
add_v_lines(axis6, just_gap_down)
axis6.set_title('Distribution of stocks per day\n which satisfy gap down cond for long')

plt.tight_layout()

plt.show()
