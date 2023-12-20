#!/usr/bin/env python
from typing import Callable, List
def euler(x0 : float, y0 : float, f : Callable, h : float, m : int) -> List[List[float]]:
    
    x = [x0]
    y = [y0]

    for j in range(m):
        x.append(x[j]+h)
        y.append(y[j]+h*f(x[j],y[j]))
    
    return [x,y]