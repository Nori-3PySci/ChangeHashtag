# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import os

if os.path.exists('./new') == False:
    os.mkdir('new')

for file in os.listdir('./'):
    if file[-4:] == '.txt':
        filename = file
        with open(file, 'r') as f_in:
            for row in f_in:
                if '駆け出し' in row:
                    row = '#エンジニアと繋がりたい'
        
                with open('./new/' + filename, 'a') as f_out:
                    f_out.write(row)
# -


