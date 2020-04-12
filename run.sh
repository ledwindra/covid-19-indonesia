#!/bin/bash

git pull origin master
pip3 install -r requirements.txt
python3 src/jawa_timur.py
jupyter nbconvert --execute index.ipynb 
jupyter nbconvert index.ipynb --to slides
mv index.slides.html index.html
git add .
git commit -m "added stuffs"
git push origin master