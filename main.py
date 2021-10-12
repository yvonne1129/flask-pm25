from flask import Flask
from datetime import datetime

from flask.templating import render_template
from scrape.pm25 import get_pm25
import json

#modify by remote

# __name__=main.py等於類別的初始執行__init__
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return render_template('index.html', time=time)
# GET取值

# @app.route('/sum/x=<int:x>&y=<int:y>')
# def get_sum(x, y):
    # return f'total:{x+y}'

# post 函式


@app.route('/pm25-data', methods=['POST'])
def pm25_data():
    columns, datas = get_pm25()
    print(columns, datas)
    sites, values = [], []
    for data in datas:
        sites.append(data[0])
        values.append(data[-1])
    data = {'sites': sites, 'values': values}

    return json.dumps(data, ensure_ascii=False)


@app.route('/pm25-echarts')
def pm25_echarts():
    return render_template('pm25-echarts.html')


@app.route('/echarts')
def echarts():
    return render_template('echarts.html')


@app.route('/pm25')
def pm25():
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    columns, datas = get_pm25(sort=True)
    return render_template('pm25.html', **locals())


@app.route('/stock')
def stock():
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    stocks = [
        {'分類': '日經指數', '指數': '22,920.30'},
        {'分類': '韓國綜合', '指數': '2,304.59'},
        {'分類': '香港恆生', '指數': '25,083.71'},
        {'分類': '上海綜合', '指數': '3,380.68'}
    ]

    return render_template('stock.html', time=time, stocks=stocks)


@app.route('/sum/x=<x>&y=<y>')
def get_sum(x, y):
    return f'total:{eval(x)+eval(y)}'


@app.route('/today/<string:name>')
def detToday(name):
    print(datetime.now())
    # 字串
    return name+""+datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    app.run(debug=True)
