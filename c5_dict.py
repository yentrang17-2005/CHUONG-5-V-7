# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:55:38 2024

@author: Admin
"""

n = int(input('Nhập giá trị nguyên n: '))
dict = {}
i = 1
while i <= n:
    dict[i]= i**i
    i += 1
print(dict)