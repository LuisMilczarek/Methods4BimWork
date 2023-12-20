#!/usr/bin/env python
import os
import matplotlib.pyplot as plt
from edo import euler

def dy(x : float, y : float) -> float:
    return x-y+2

def main() -> None:
    BASE_PATH = "./graficos"
    if not os.path.exists(BASE_PATH):
        os.mkdir(BASE_PATH)
    X0 = 0
    Y0 = 2
    H = 0.05
    M = 20
    x,y = euler(X0, Y0,dy,H,M)

    plt.plot(x,y)
    plt.savefig(f"{BASE_PATH}/euler.png")



if __name__ == "__main__":
    main()