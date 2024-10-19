# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:14:44 2024

@author: Admin
"""
n=int(input('Nhập số nguyên dương N:'))
giaithua=1
for i in range (1,n+1):
    giaithua=giaithua*i 
print(n,"\b!=",giaithua)