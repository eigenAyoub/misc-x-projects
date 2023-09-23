import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    # have path of the csv as argument when dealing with multiple csv files.
    return pd.read_csv("data2.csv", 
                       sep=";", 
                       decimal = ",", 
                       thousands='.').drop(["Unnamed: 0"], axis=1)

def plot_data(data, column):
    # since we are only plotting one col, we can just pass the col. itself
    # instead of passing the whole data + index.
    # TODO

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(data['t_(s)'], data.iloc[:, column], label=data.columns[column])
    ax.set_title(f'Time Series: {data.columns[column]}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')

    interval = 100  
    #TODO: Adjust this interval as needed

    x_ticks = data['t_(s)'][::interval]
    ax.set_xticks(x_ticks)

    ax.legend()
    plt.show()


def describe(data):
    # this could just be done right from main, since, we are  \\
    # already loading the data there... but I\ll keep it here for now.
    return data.describe() 


## advanced plotting: Moving average // Resample.

## some modeling?
