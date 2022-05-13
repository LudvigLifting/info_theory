import numpy as np

def G(r: int, m: int):

    if r < 0 or m < 0:
        return
    
    if r == 0:
        return np.array([1 for _ in range(2**m)])
    elif r == m:
        return np.identity(2**m, dtype=int)

    if r > 1:
        return np.array([[G(r, m - 1), G(r, m - 1)], [np.zeros((r - 1, m - 1), dtype=int), G(r - 1, m - 1)]], dtype=object)
    else:
        return np.array([[G(r, m - 1), G(r, m - 1)], [np.zeros((1, m - 1), dtype=int), G(r - 1, m - 1)]], dtype=object)


if __name__ == '__main__':
    print(np.zeros((0, 2), dtype=int))
    print(np.stack(G(1, 3)))
