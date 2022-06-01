#! /bin/bash

cp -a ./oi-wiki/docs docs
python3 get-nav.py
mkdocs build -v
npx mathjax-render-for-mkdocs-material --srcDir=./site --useWorker
