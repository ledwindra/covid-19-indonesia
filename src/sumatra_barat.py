import os
import requests
import pandas as pd

class SumatraBarat:

    def __init__(self, url):
        self.url = url

    def get_json(self):
        res = requests.get(self.url)

        return res.json()

    def get_dataframe(self):
        data = self.get_json()
        df = pd.DataFrame([])
        for i in range(len(data['features'])):
            df = pd.concat([df, pd.DataFrame([data['features'][i]['attributes']])])
        df = df.reset_index(drop=True)

        return df

def main():
    df = SumatraBarat('https://services8.arcgis.com/GQkhBJkczZpSe3lX/arcgis/rest/services/Corona_Sumbar/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outSR=102100&resultOffset=0&resultRecordCount=19&cacheHint=true').get_dataframe()
    return df.to_csv('./data/sumatra-barat.csv', index=False)

if __name__ == '__main__':
    main()