import threading
from math import ceil
from time import ctime, time

MINUTE_DATA_DIR = '../data/minute/'
FIVE_MINUTE_DATA_DIR = '../data/5minutes/'
FIFTEEN_MINUTE_DATA_DIR = '../data/15minutes/'
DAILY_DATA_DIR = '../data/daily/'
WEEKLY_DATA_DIR = '../data/weekly/'
TICK_DATA_DIR = '../data/ticks'
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


def split_into_chunck(data_list, chunck_size=100):
    l = len(data_list)
    n = ceil(l / chunck_size)
    deck = list()
    for i in range(n):
        if ((1 + i) * chunck_size) < l:
            deck.append(data_list[i * chunck_size:(i + 1) * chunck_size])
        else:
            deck.append(data_list[i * chunck_size:])
    print('Total length:', l)
    print('Chunck size:', chunck_size)
    print('Number of chuncks:', deck.__len__())
    return deck


def parallel_processing(tasks, processing_func, chunck_size=100, params=None):
    chuncks = split_into_chunck(tasks, chunck_size)
    threads = list()
    for i in range(len(chuncks)):
        th = threading.Thread(target=processing_func, args=(chuncks[i], params))
        threads.append(th)
    start = time()
    print('Start at:', ctime())
    print(len(threads))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end = time()
    print('End at:', ctime())
    print('Duration:', round(end - start, 2))
