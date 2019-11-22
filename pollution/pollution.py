# 我们可以使用这些数据，并构建一个预测问题，在前一天的天气条件和污染情况下，我们预测下一个小时的污染情况
from pandas import read_csv
from datetime import datetime
# 加载数据
def parse(x):
    return datetime.strptime(x, '%Y %m %d %H')
dataset = read_csv('pollution1.csv',  parse_dates = [['year', 'month', 'day', 'hour']], index_col=0, date_parser=parse)
dataset.drop('No', axis=1, inplace=True)
# 手动更改列名
dataset.columns = ['pollution', 'dew', 'temp', 'press', 'wnd_dir', 'wnd_spd', 'snow', 'rain']
dataset.index.name = 'date'
# 把所有NA值用0替换
dataset['pollution'].fillna(0, inplace=True)
# 丢弃前24小时
dataset = dataset[24:]
# 输出前五行
print(dataset.head(5))
# 保存到文件中
dataset.to_csv('pollution2.csv')