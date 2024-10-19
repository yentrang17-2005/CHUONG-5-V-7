# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:41:44 2024

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:45:07 2024

@author: Admin
"""

import math
def chuvi_dt(hinh,pheptinh,*args,**kwargs):
    if hinh == "vuong":
        canh = args [0]
        return 4*canh if pheptinh == "chuvi" else canh*canh
    elif hinh == "chunhat":
        dai = args [0]
        rong = args [1]
        return 2*(dai+rong) if pheptinh == "chuvi" else dai*rong
    elif hinh == "tron":
        bankinh = args [0]
        return 2*math.pi*bankinh if pheptinh == "chuvi" else bankinh**2*math.pi
    else:
        return "hinh khong hop le"

if __name__=="__main__":
    print("chuvihinhvuong:", chuvi_dt('vuong','chuvi',3))
    print("dientichinhvuong:", chuvi_dt('vuong','dt',3)) 
                              
    print("chuvihinhchunhat:", chuvi_dt('chunhat','chuvi',3,4))
    print("dientichhinhchunhat:", chuvi_dt('chunhat','dt',3,4)) 
    
    print("chuvihinhtron:", chuvi_dt('tron','chuvi',3))
    print("dientichinhtron:", chuvi_dt('tron','dt',3)) 