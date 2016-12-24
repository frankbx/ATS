import math
from time import time, ctime

from AnalysisEngine import *


class AnalysisEngine():
    def __init__(self, ktype='D', start=None, end=None):
        self.start = start
        self.end = end
        self.ktype = ktype
        self.directory = DATA_DIR_DICT[self.ktype]
        self.basics = get_basics()

    def cal_sharpe_ratio(self, code):
        data = load_stock_data(code, self.ktype, self.start, self.end)
        sharpe_ratio = None
        if data is not None and len(data) > 0:
            data['daily_return'] = (data.close - data.close.shift(1)) / data.close.shift(1)
            data['excess_daily_return'] = data.daily_return - RISK_FREE_RATE / YEARLY_TRADING_DAYS
            sharpe_ratio = math.sqrt(YEARLY_TRADING_DAYS) * data.mean().ix['excess_daily_return'] / data.std().ix[
                'excess_daily_return']
            print(code, sharpe_ratio, data.date[0])
        return code, sharpe_ratio, data.date[0]

    def cal_sharpe_ratio_all(self):
        codes = self.basics.index
        d = {'code': [], 'sharpe_ratio': [], 'timeToMarket': []}
        start = time()
        print('Start at:', ctime())
        for code in codes:
            c, s, t = self.cal_sharpe_ratio(code)
            d['code'].append(c)
            d['sharpe_ratio'].append(s)
            d['timeToMarket'].append(self.basics.ix[code].timeToMarket)
        df = pd.DataFrame.from_records(data=d)
        df.to_csv('sharpe_ratio.csv', index=False)
        end = time()
        print('End at:', ctime())
        print('Duration:', round(end - start, 2))

    def get_day_overview(self, day):
        pass

if __name__ == '__main__':
    engine = AnalysisEngine()
    engine.cal_sharpe_ratio_all()
