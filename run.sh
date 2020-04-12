jupyter nbconvert index.ipynb --to slides --post serve
mv index.slides.html index.html
git add .
git commit -m "added stuffs"
git push origin master