#!/usr/bin/env python

import argparse
import wind_data_utils

def main():

    # init. the parser
    parser = argparse.ArgumentParser(description='Wind Data Analysis')

    # CLI arguments of some actions
    parser.add_argument('--plot', action='store_true', 
                        help='Plot wind data')

    # TODO: Add subcommands for the moving average / resampling plotting.

    parser.add_argument('--describe', action='store_true', 
                        help='Statistical desc. of the DB')
    parser.add_argument('--columns', nargs='+', 
                        help='Specify columns to plot')

    args = parser.parse_args()
    # this past call, gets the Namespace of the arguments



    # to avoid loading the data with every call/action. 
    # we will load it here.
    data = wind_data_utils.load_data()

    if args.plot:
        if not args.columns:
            print("Please specify the column index to plot  --columns.")
        else:
            #data = wind_data_utils.load_data('data2.csv')
            wind_data_utils.plot_data(data,int(args.columns[0]))
    if args.describe:
        #data = wind_data_utils.load_data('data2.csv')
        print(wind_data_utils.describe(data))

if __name__ == "__main__":
    main()

