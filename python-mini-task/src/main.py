#!/usr/bin/env python

import argparse
import wind_data_utils

def main():
    # init. the parser and subparser
    parser = argparse.ArgumentParser(description='Wind Data Analysis')
    subparsers = parser.add_subparsers(title='Available Actions', dest='action')
    
    # subparsers (i.e., actions)  
    plot_parser = subparsers.add_parser('plot', help='Plot wind data')
    subparsers.add_parser('describe', help='Plot wind data')

    # arguments for --plot 
    plot_parser.add_argument('--columns', nargs='+', help='Specify column to plot')
    plot_parser.add_argument('--rolling-avg', action='store_true')
    plot_parser.add_argument('--resample', action='store_true')
    
    # get Namespace of the arguments
    args = parser.parse_args()

    # we will load it here.
    data = wind_data_utils.load_data()

    if args.action == 'plot':
        if not args.columns:
            print("Please specify the column index to plot  --columns.")
        else:
            if args.resample:
                wind_data_utils.plot_resample(data, int(args.columns[0]))
            elif args.rolling_avg:
                wind_data_utils.plot_rolling(data, int(args.columns[0]))
            else:
                wind_data_utils.plot_data(data, int(args.columns[0]))
                


    if args.action == 'describe':
        
        #data = wind_data_utils.load_data('data2.csv')
        print(wind_data_utils.describe(data))

if __name__ == "__main__":
    main()

