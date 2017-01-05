import os
import threading
from datetime import date
from time import ctime, time

import pandas as pd
import tushare as ts

from DataEngine import *

'''
Web Data Engine is supposed to retrieve data from internet using Tushare library.
'''


class WebDataEngine():
    def __init__(self, ktype='D'):
        print(ts.__version__)
        self.ktype = ktype
        self.directory = DATA_DIR_DICT[self.ktype]
        basics = ts.get_stock_basics()
        self.basics = basics[basics.timeToMarket != 0]
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

    def init_data_warehouse(self):
        chuncks = split_into_chunck(self.basics.index, 200)
        threads = list()
        for i in range(len(chuncks)):
            th = threading.Thread(target=self.download_data, args=chuncks[i])
            threads.append(th)
        start = time()
        print('Start at:', ctime())
        # print(len(threads))
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        end = time()
        print('End at:', ctime())
        print('Duration:', round(end - start, 2))

    def download_data(self, *code_list):
        # print(len(code_list))
        for code in code_list:
            # print(code)
            self.get_online_data(code)

    def get_online_data(self, code, start=None, end=None):
        filename = self.directory + add_suffix(code) + '.csv'
        # print(code)
        # check if the file already exists
        if os.path.exists(filename):
            # get the latest date
            existing_data = pd.read_csv(filename)
            row, col = existing_data.shape
            latest_date = existing_data.date[row - 1]
            # retrieve data from the latest date
            data = ts.get_k_data(code=code, ktype=self.ktype, start=latest_date, retry_count=30, pause=2)
            # print(data, data.shape)
            r, c = data.shape
            # discard duplicated data of the last day if there's more than 1 row
            if r > 1:
                # Locate by integer, not index
                delta_data = data.iloc[1:r].copy()
                # Append data to the file
                delta_data.to_csv(filename, mode='a', header=None, index=False)
                print(code, 'updated')
        else:
            time_to_mkt = str(self.basics.ix[code]['timeToMarket'])
            start_date = time_to_mkt[0:4] + '-' + time_to_mkt[4:6] + '-' + time_to_mkt[6:8]
            # Create the data file directly
            data = ts.get_k_data(code=code, ktype=self.ktype, start=start_date, retry_count=20, pause=1)
            # Data can be None if it's a new stock
            if data is not None:
                # The data is sorted so that the latest data at the bottom of the file.
                # It's easier to append future data while keep the ascending order of date
                data.sort_index(axis=0, inplace=True)
                data.to_csv(filename, index=False)
                print(code, 'created')

    # TODO add logic to avoid duplicate update
    def get_market_data(self):
        today = ts.get_today_all()
        today['date'] = str(date.today())
        if os.path.exists('daily_overview.csv'):
            today.to_csv('daily_overview.csv', mode='a', encoding='utf8', index=False, header=False)
        else:
            today.to_csv('daily_overview.csv', encoding='utf8', index=False)

    # TODO add logic to avoid duplicate update
    def get_basics(self):
        basics = ts.get_stock_basics()
        basics['date'] = str(date.today())
        if os.path.exists('basics.csv'):
            basics.to_csv('basics.csv', mode='a', encoding='utf8', header=False)
        else:
            basics.to_csv('basics.csv', encoding='utf8')

    #TODO add code to use multiple threads
    def get_no_fq_data(self):
        codes = self.basics.index
        directory = '../data/daily_bfq/'
        if not os.path.exists(directory):
            os.mkdir(directory)
        for code in codes:
            filename = directory + add_suffix(code) + '.csv'
            if os.path.exists(filename):
                # get the latest date
                existing_data = pd.read_csv(filename)
                row, col = existing_data.shape
                latest_date = existing_data.date[row - 1]
                # retrieve data from the latest date
                data = ts.get_hist_data(code=code, ktype=self.ktype, start=latest_date, retry_count=30, pause=2)
                data.sort_index(inplace=True)
                # print(data, data.shape)
                r, c = data.shape
                # discard duplicated data of the last day if there's more than 1 row
                if r > 1:
                    # Locate by integer, not index
                    delta_data = data.iloc[1:r].copy()
                    delta_data['code'] = code
                    # Append data to the file
                    delta_data.to_csv(filename, mode='a', header=None)
                    # print(delta_data)
                    print(code, 'updated auttype None')
            else:
                data = ts.get_hist_data(code, ktype=self.ktype, retry_count=20, pause=2)
                data['code'] = code
                data.sort_index(axis=0, inplace=True)
                data.to_csv(filename)
                print(code, 'created auttype None')


if __name__ == '__main__':
    engine = WebDataEngine()
    engine.get_basics()
    engine.get_market_data()
    engine.get_no_fq_data()
    engine.init_data_warehouse()
