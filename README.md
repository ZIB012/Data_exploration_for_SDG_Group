# Sales Data Analysis

This repository contains a Jupyter notebook that explores a dataset related to the sales of products from two different shops. The analysis aims to provide insights into sales trends, product popularity, and inventory management. 

The .csv dataset file is not present in the repository due to privacy issues.

## Table of Contents

- [Installation](#installation)
- [Libraries Used](#libraries-used)
- [Usage](#usage)
- [Notebook Overview](#notebook-overview)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run the notebook, you need to have Python and Jupyter Notebook installed. You can install the necessary Python libraries using the following command:

## Libraries Used

- `pandas`: For data manipulation and analysis.
- `matplotlib`: For creating static, animated, and interactive visualizations.
- `seaborn`: For making statistical graphics.
- `numpy`: For numerical computations.
- `collections.Counter`: For counting hashable objects.
- `ast`: For processing Python abstract syntax trees.
- `util_functions`: A self-written library containing utility functions used in the analysis.

### util_functions
- _util.plot_total_sales(DataTable, label_date='date_dt', label_plot='sales_qt', label_groups='', group_value='')_ is the function used to plot the total sales over time. Using the attributes _label\_groups_ and _group\_value_ one is able to consider only a certain type of sales, for example considering only a single store.

- _util.groupby_sum_plot(DataTable, group, target_plot, title='', nlargest=-1, xlabel='', ylabel='')_ is the function used to bar-plot the dataset. The attributes are:
    - group: the dataset feature for which the DataTable is grouped-by
    - target\_plot: the dataset feature that is plotted
    - nlargest: it considers only the top n values in descending order
    - xlabel, ylabel: if these attributes remain equalt to '', then in the plot label the values of _group_ and _target\_plot_ are set

- _plot_size_stock_vs_sold(DataT_available, DataT_sold, product_type, size)_ is the function used to time-plot the availability and sales for each product type and size


## Usage

1. Clone the repository to your local machine:
    ```bash
    git clone https://https://github.com/ZIB012/Data_exploration_for_SDG_Group.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Data_exploration_for_SDG_Group
    ```
3. Open the Jupyter notebook:
    ```bash
    jupyter notebook main.ipynb
    ```


## Notebook Overview

The notebook is structured into several key sections:

0. **Load Dataset**: The dataset is loaded into a pandas dataframe and its features are observed
1. **Time-dependent sales plots**: Visualizes sales trends over time. The total sales for each store are plotted and the different stores are compared. 
2. **Regular versus promo sales**: Compares regular sales and promotional sales over time. A huge peak is observed, that it could have helped the stores to be known by the customers.
3. **Top 10 products sold**: Identifies the top-selling products.
4. **Total Sales for each brand and stores**: Summarizes total sales by brand and store. There's a clear gap between the two brands present in the dataset.
5. **Stock vs sold products' sizes**: Analyzes the relationship between available stock sizes and products' sizes sold. Some products' types are more relevant than others.
6. **Size availability**: Examines the availability of different product sizes.

Each section includes visualizations and analyses to provide insights into the dataset.


