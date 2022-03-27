#! /bin/bash

cp -a ./oi-wiki/docs docs
python3 get-nav.py
mkdocs serve -v
