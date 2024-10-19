# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:40:42 2024

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:12:19 2024

@author: Admin
"""
import math
def chuvi(hinh,*args,**kwargs):
    if hinh == "vuong":
        canh = args [0]
        return 4*canh 
    elif hinh == "chunhat":
        dai = args [0]
        rong = args [1]
        return 2*(dai+rong) 
    elif hinh == "tron":
        bankinh = args [0]
        return 2*math.pi*bankinh 
    else:
        return "hinh khong hop le"

if __name__=="__main__":
    print("chuvihinhvuong:", chuvi('vuong',3))
    print("chuvihinhchunhat:", chuvi('chunhat',3,4))
    print("chuvihinhtron:", chuvi('tron',3))
    