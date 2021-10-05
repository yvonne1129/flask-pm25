import pandas as pd

url = 'https://data.epa.gov.tw/api/v1/aqx_p_322?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv'


def get_pm25():
    df = pd.read_csv(url).dropna()
    columns = ['SiteName', 'County', 'Concentration']
    datas = sorted(df[columns].values.tolist(),
                   key=lambda x: x[-1], reverse=True)

    return columns, datas


if __name__ == "__main__":
    print(get_pm25())
