# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:26:23 2024

@author: Admin
"""

import random
a = random.randint(20, 30)
print("Số lượng phần tử: ", a)




danh_sach = [0] * a 
for i in range(a):
   so_thuc = random.uniform(18, 99)
   danh_sach[i]= so_thuc ** 2   
print("Danh sách các giá trị bình phương:", danh_sach)

