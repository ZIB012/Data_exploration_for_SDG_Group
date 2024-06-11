import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
from collections import Counter
import ast
warnings.filterwarnings('ignore')


def Single_Values_of_a_DataTable(DataT):
    Dictionary_Single_Values = {}
    for i in DataT.columns:
        single_values = []

        for j in DataT[i]:

            if len(single_values) == 0:
                single_values.append(j)

            elif j not in single_values:
                single_values.append(j)
        Dictionary_Single_Values[i] = single_values
    
    return Dictionary_Single_Values

def groupby_sum_plot(Table, group, target_plot, title='', nlargest=-1, xlabel='', ylabel=''):
    x_groupby = Table.groupby(group)[target_plot].sum()

    if nlargest > 0:
        x_groupby = x_groupby.nlargest(nlargest)

    plt.figure(figsize=(12, 6))
    x_groupby.plot(kind='bar')
    plt.title(title)
    plt.xlabel(group if xlabel=='' else xlabel)
    plt.ylabel(target_plot if xlabel=='' else ylabel)
    plt.grid(True)
    plt.show()

def function_DataTable_sizes_and_sold(DataT, sizes_for_each_type, label_date='date_dt',
                                       label_type='size_range_cd', label_stock='size_in_stock', label_sold='size_sold_qt'):
    
    product_types = Single_Values_of_a_DataTable(DataT)[label_type]
    DataTable_sizes_availability = {}
    DataTable_sizes_sold = {}
    single_DataTable_availability = DataT

    for product_type in product_types:
        DataTable_sizes_availability[product_type] = {}
        DataTable_sizes_sold[product_type] = {}

        filtered_Table = DataT[DataT[label_type] == product_type]

        sizes = sorted(list(sizes_for_each_type[product_type].keys()))

        for sz in sizes:
            single_DataTable_availability[f'is_{sz}_in_stock'] = filtered_Table[label_stock].apply(lambda x: f'{sz}' in x)
            single_DataTable_availability[f'is_{sz}_sold'] = filtered_Table[label_sold].apply(lambda x: f'{sz}' in x)

            DataTable_sizes_availability[product_type][sz] = single_DataTable_availability.groupby(label_date)[f'is_{sz}_in_stock'].sum()
            DataTable_sizes_sold[product_type][sz] = single_DataTable_availability.groupby(label_date)[f'is_{sz}_sold'].sum()
    
    return DataTable_sizes_availability, DataTable_sizes_sold

def plot_size_stock_vs_sold(DataT_available, DataT_sold, product_type, size):
    plt.figure(figsize=(12, 6))
    DataT_available[product_type][size].plot(label='Stock')
    DataT_sold[product_type][size].plot(label='Sold')
    plt.title(f'Size Availability vs Size Sells\nProduct Type: {product_type} || Size: {size}')
    plt.xlabel('Date')
    plt.ylabel('Sold vs Stock')
    plt.grid(True)
    plt.legend(prop={'size': 12})
    plt.show()

def function_DataTable_product_stock_and_sold(DataT, label_date='date_dt',
                                              label_type='sku_cd', label_stock='size_in_stock', label_sold='size_sold_qt'):
    
    product_types = Single_Values_of_a_DataTable(DataT)[label_type]
    DataTable_sizes_availability = {}
    DataTable_sizes_sold = {}
    single_DataTable_availability = DataT

    for product_type in product_types:
        DataTable_sizes_availability[product_type] = {}
        DataTable_sizes_sold[product_type] = {}

        filtered_Table = DataT[DataT[label_type] == product_type]

        single_DataTable_availability[f'is_{product_type}_in_stock'] = filtered_Table[label_stock].apply(lambda x: f'{product_type}' in x)
        single_DataTable_availability[f'is_{product_type}_sold'] = filtered_Table[label_sold].apply(lambda x: f'{product_type}' in x)

        DataTable_sizes_availability[product_type][product_type] = single_DataTable_availability.groupby(label_date)[f'is_{product_type}_in_stock'].sum()
        DataTable_sizes_sold[product_type][product_type] = single_DataTable_availability.groupby(label_date)[f'is_{product_type}_sold'].sum()
    
    return DataTable_sizes_availability, DataTable_sizes_sold

def plot_product_stock_vs_sold(DataT_available, DataT_sold, product_type, size):
    plt.figure(figsize=(12, 6))
    DataT_available[product_type][size].plot(label='Stock')
    DataT_sold[product_type][size].plot(label='Sold')
    plt.title(f'Product Code: {product_type} \n Size: {size}')
    plt.xlabel('Data')
    plt.ylabel('Sold vs Stock')
    plt.grid(True)
    plt.legend(prop={'size': 12})
    plt.show()

def plot_total_sales(DataT, label_date='date_dt', label_plot='sales_qt', label_groups='', group_value=''):

    if label_groups != '':
        Data = DataT[DataT[label_groups] == group_value]
    else:
        Data = DataT

    plt.figure(figsize=(12, 6))
    Data.groupby(label_date)[label_plot].sum().plot()

    if label_groups != '':
        plt.title(f'Total sales distribution over time\n{label_groups} = {group_value}')
    else:
        plt.title('Total sales distribution over time')

    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.show()