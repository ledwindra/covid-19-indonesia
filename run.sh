jupyter nbconvert index.ipynb --to slides
mv index.slides.html index.html
git add .
git commit -m "added stuffs"
git push origin master