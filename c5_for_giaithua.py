# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:14:31 2024

@author: Admin
"""

n=int(input('Nhập số nguyên dương N: '))
giaithua = 1
for i in range (1,n+1):
    giaithua*=i
print(n,"\b!=",giaithua)

