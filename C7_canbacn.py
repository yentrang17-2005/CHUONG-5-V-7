

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:02:05 2024

@author: Admin
"""




def canbac_n(x,n):
    return x**(1/n)
    
    
def binhphuong(n):
    if n>0:
        return n**2
    else:
        return "số không hợp lệ"
    
def sochan_am(n):
    return n<0 and n%2 ==0


def ktra_so (n):
    if n < 0 and n%2!=0:
        return -1
    elif n > 0 and n%2 ==0:
        return 1
    return 0


def ktra_giatri():
    n = input("nhap n: ")
    if n.replace('.','',1).replace('-','',1).isdigit():
        n= float (n)
    
    #if n.lstrip('-').isdigit(): (-)123
        #n  = int(n)
    #if n.strip('-').isdigit(): (-)123(-)(-nếu chuỗi)
        #n = int(n)

    if -89 <= n <=90:
        return n 
    print('không hợp lệ, nhập lại:')
    return ktra_giatri()
        
if __name__=="__main__":
    print(canbac_n(8,3))
    print(binhphuong(3))
    print(sochan_am(4))
    print(ktra_so(5))
    print(ktra_giatri())