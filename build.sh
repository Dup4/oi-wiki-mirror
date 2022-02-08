#! /bin/bash

python3 get-nav.py
mkdocs build -v
npx mkdocs-render-math-ssr --srcDir=./site --useWorker
