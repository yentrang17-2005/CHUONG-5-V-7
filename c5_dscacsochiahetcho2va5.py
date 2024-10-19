# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:48:37 2024

@author: Admin
"""

a = 2018
b = []
while a <= 2828:
    if a % 2 == 0 and a % 5 == 0:
        b += [a]
    a += 1
print('Danh sách các số chẵn nguyên và chia hết cho 5 từ 2018 - 2828:',b)