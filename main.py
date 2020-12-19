import numpy as np


def derivation(x, func):
    dx = 0.00001
    return round((func(x+dx) - func(x))/dx, 2)


def gradient(x, func):
    dx = 0.00001
    return [round((func([x[0]+dx, x[1]]) - func(x))/dx, 2), round((func([x[0], x[1]+dx]) - func(x))/dx, 2)]


def gradient_optimization_one_dim(func):
    e = 0.001
    x = 10
    dx = 0.00001
    i = 0
    while i < 51:
        y = (func(x+dx) - func(x))/dx
        #print(i, x, func(x), y)
        if abs(y) <= e or i == 50:
            break
        #elif y > 0:
        #    x = x - e*y
        else:
            x = x - e*y
        i +=1
    #print("return ", i, x, func(x), y)
    return round(x, 2)


def gradient_optimization_multi_dim(func):
    e = 0.001
    x = [4,10]
    dx = 0.00001
    ix = 0
    iterCnt = 50
    while ix < iterCnt+1:
        y = [(func([x[0]+dx, x[1]]) - func(x))/dx, (func([x[0], x[1]+dx]) - func(x))/dx]
        #print(ix, x, func(x), y)
        if (abs(y[0]) <= e and abs(y[1]) <= e) or ix == iterCnt:
            break
        if abs(y[0]) > e:
            x[0] = x[0] - round(e*y[0], 2)
        if abs(y[1]) > e:
            x[1] = x[1] - round(e*y[1], 2)
        ix +=1
        
    #print("return ", ix, x, func(x), y)
    return [round(x[0], 2), round(x[1], 2)]
