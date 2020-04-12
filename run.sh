#!/bin/bash

git pull origin master
pip3 install -r requirements.txt

python3 src/aceh.py
python3 src/sumatra_barat.py
python3 src/jawa_timur.py

jupyter nbconvert index.ipynb --to slides
mv index.slides.html index.html
git add .
git commit -m "added stuffs"
git push origin master