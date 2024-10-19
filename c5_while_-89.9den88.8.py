# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:41:00 2024

@author: Admin
"""

value = None 
while value is None or not (-89.9 <= value <= 88.8):
    n = input('Nhập một số trong đoạn [-89.9;88.8]: ').strip()
    if n and n.replace('-','',1).replace('.','',1).isdigit():
        value = float(n)
    else:
        print('Giá trị không hợp lệ, vui lòng nhập lại.')
if -89.9 <= value <= 88.8:
    print(f'Giá trị hợp lệ: {value}')
    