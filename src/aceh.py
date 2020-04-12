import os
import requests
import pandas as pd

class Aceh:

    def __init__(self, url):
        self.url = url

    def get_json(self):
        res = requests.get(self.url)

        return res.json()

    def get_dataframe(self):
        df = pd.DataFrame(self.get_json())

        return df

def main():
    df = Aceh('https://covid.bravo.siat.web.id/json/covid').get_dataframe()
    return df.to_csv('./data/aceh.csv', index=False)

if __name__ == '__main__':
    main()

