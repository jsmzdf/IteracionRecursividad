# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
def fibo(num):
    if num<= 2:return 1
    return fibo(num-1) + fibo(num-2)
def pot(num,exp):
    if exp ==0:return 1
    if exp ==1: return num
    return pot(num,exp-1)*num
def div(dividendo,divisor):
    if divisor>dividendo:return 0
    return div((dividendo-divisor),divisor)+1
def fiboI(num):
     a, b = 0,1
     while a < num:
        a, b = b, a+b
     return a
def potI(num,exp):
    if exp ==0:return 1
    if exp ==1: return num
    resultado=num
    for i in range(exp-1):resultado=resultado*num
    return resultado
def divI(dividendo,divisor):
    if divisor>dividendo:return 0
    a=0
    while 0 < dividendo:
        a=a+1
        dividendo=dividendo-divisor
    return a
    
if __name__ == '__main__':
    print("Función recurisva fibonacci")          
    print(fibo(6))
    print("Función recursiva potencia")
    print(pot(3,2))
    print("Función recursiva división")
    print(div(10,2))
    print("Función iterativa fibonacci")          
    print(fiboI(6))
    print("Función iterativa potencia")
    print(potI(2,3))
    print("Función iterativa división")
    print(divI(50,2))
