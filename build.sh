#! /bin/bash

cp -a ./oi-wiki/docs docs
python3 get-nav.py
mkdocs build -v
npx mkdocs-render-math-ssr --srcDir=./site --useWorker
