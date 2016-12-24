from math import ceil

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
