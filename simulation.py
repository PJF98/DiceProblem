import matplotlib.pyplot as plt

import numpy as np

def init_arr(n):
    arr = np.zeros([6 * n + 1, n + 1])
    for x in range(6 * n + 1):
        for y in range(n + 1):
            if y == 0:
                if x == 0:
                    arr[x, y] = 3.5
            else:
                value = x / y
                if value > 6:
                    arr[x, y] = 0
                elif value < 1:
                    arr[x, y] = 0
                elif value > 3.5:
                    arr[x, y] = value
                else:
                    arr[x, y] = 3.5
    return arr

def apply_transformation(arr, n):
    newarr = arr.copy()
    for x in range(6 * n + 1):
        for y in range(n + 1):
            if y == 0:
                if x == 0:
                    newarr[x, y] = 1/6 * np.sum([arr[x+i, y+1] for i in range(1, 7)])
            else:
                value = x / y
                if value > 6:
                    newarr[x, y] = 0
                elif value < 1:
                    newarr[x, y] = 0
                elif y + 1 < n:
                    newarr[x, y] = 1/6 * np.sum([arr[x+i, y+1] for i in range(1, 7)])
    return np.maximum(newarr, arr)

if __name__ == "__main__":
    EVs = np.zeros(50)
    for n in range(1, 51):
        arr = init_arr(n)
        for _ in range(n):
            arr = apply_transformation(arr, n)
        EVs[n - 1] = arr[0, 0]
    plt.plot(EVs)
    plt.xlabel("Number of rolls")
    plt.ylabel("EV")
    plt.show()
