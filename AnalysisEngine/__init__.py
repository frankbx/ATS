import numpy as np
import pandas as pd
import os

RISK_FREE_RATE = 0.04
YEARLY_TRADING_DAYS = 252
MINUTE_DATA_DIR = '../data/minute/'
FIVE_MINUTE_DATA_DIR = '../data/5minutes/'
FIFTEEN_MINUTE_DATA_DIR = '../data/15minutes/'
DAILY_DATA_DIR = '../data/daily/'
WEEKLY_DATA_DIR = '../data/weekly/'
K_TYPES = ['m', '5', 'D', 'W', '15']
DATA_DIR_DICT = {
    'D': DAILY_DATA_DIR,
    'W': WEEKLY_DATA_DIR,
    'm': MINUTE_DATA_DIR,
    '5': FIVE_MINUTE_DATA_DIR,
    '15': FIFTEEN_MINUTE_DATA_DIR
}


def add_suffix(code):
    if code.startswith('6'):
        return code + '.SH'
    else:
        return code + '.SZ'


def load_stock_data(code, ktype='D', start=None, end=None):
    directory = DATA_DIR_DICT[ktype]
    data = None
    filename = directory + add_suffix(code) + '.csv'
    if os.path.exists(filename):
        data = pd.read_csv(filename)
        data.index = data.date
    return data


def get_basics():
    basics = pd.read_csv('../DataEngine/basics.csv', dtype={'code': np.str})
    basics = basics[basics.timeToMarket != 0]
    basics.index = basics.code
    return basics
