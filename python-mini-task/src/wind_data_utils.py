import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    # have path of the csv as argument when dealing with multiple csv files.
    return pd.read_csv("output.csv", sep = ";", parse_dates=True)

def plot_data(data, column):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(data['t_[(s)]'], data.iloc[:, column], label=data.columns[column])
    ax.set_title(f'Time Series: {data.columns[column]}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')

    interval = 100  

    #TODO: Adjust this interval as needed

    x_ticks = data['t_[(s)]'][::interval]
    ax.set_xticks(x_ticks)

    ax.legend()
    plt.show()


def plot_resample(data, column):
    plt.figure(figsize=(10, 6))

    col_sampled = data.iloc[:,column].resample('2S').mean()

    plt.plot(col_sampled, marker='o')
    plt.title('2 Seconds Inteval Means')
    plt.xlabel('Time')
    plt.ylabel('Mean Value')
    plt.grid(True)
    plt.show()


def plot_rolling(data, column):
    rolling_mean = data.iloc[:,column].rolling(window=41).mean()

    plt.figure(figsize=(10, 6))
    plt.plot(data['t_[(s)]'], col, label='Original Data', alpha=0.5)
    plt.plot(data['t_[(s)]'], rolling_mean, label='Rolling Mean', color='orange')


    plt.title('Original Data with a 2 second Rolling Mean')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

def describe(data):
    # this could just be done right from main, since, we are  \\
    # already loading the data there... but I\ll keep it here for now.
    return data.describe() 


## some modeling? 
