import json
import os
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

class Jatim:
    
    def __init__(self, url):
        self.url = url
    
    def get_content(self):
        url = self.url
        res = requests.get(url)
        content = BeautifulSoup(res.content, features='html.parser')
        src = content.find_all('script')
        
        return src
    
    def get_kabupaten_data(self):
        src = self.get_content()
        kab = [x for x in src if "datakabupaten" in x.text][0].text
        kab = [x for x in kab.split('datakabupaten') if x.startswith('=[')][0]
        kab = kab.split('\n')[0]
        kab = re.split(r'[=\[\];]', kab)
        kab = [x for x in kab if len(x) > 0][0]
        kab = [x + '}' for x in kab.split('},')]
        kabs = []
        fail = []
        for k in kab:
            try:
                kabs.append(json.loads(k))
            except json.JSONDecodeError:
                fail.append(k)
        kabs.append(json.loads(fail[0][:-1]))
        
        return kabs
    
def main():
    jatim = Jatim('https://covid19dev.jatimprov.go.id/xweb/draxi')
    df = pd.DataFrame(jatim.get_kabupaten_data())
    df['id'] = df.astype({'id': 'int32'})
    df = df.sort_values(by='id')
    df['date_partition'] = datetime.now().strftime('%Y%m%d')
    df = df.drop(columns=['latitude', 'longitude', 'label_lat', 'label_lon'])
    to_decimal = lambda x: float(x.replace(',', '.'))
    lat_lon = ['lat', 'lon', 'lat1', 'lon1', 'lat2', 'lon2', 'lat3', 'lon3']

    for i in lat_lon:
        try:
            df[i] = df[i].apply(to_decimal)
        except AttributeError:
            pass

    if os.path.exists('./data/covid-jatim.csv'):
        return df.to_csv('./data/covid-jatim.csv', index=False, mode='a', header=False)
    return df.to_csv('./data/covid-jatim.csv', index=False, mode='a')

if __name__ == '__main__':
    main()