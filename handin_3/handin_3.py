import numpy as np

class Reed_Muller:

    def __init__(self):
        self.G = np.array([[1, 0, 1, 0, 1, 0, 1, 0],
                           [0, 1, 0, 1, 0, 1, 0, 1],
                           [0, 0, 1, 1, 0, 0, 1, 1],
                           [0, 0, 0, 0, 1, 1, 1, 1]], dtype=bool)

        self.permutations = np.array([[0, 0, 0, 0], 
                                      [0, 0, 0, 1], 
                                      [0, 0, 1, 0],
                                      [0, 0, 1, 1],
                                      [0, 1, 0, 0],
                                      [0, 1, 0, 1],
                                      [0, 1, 1, 0],
                                      [0, 1, 1, 1],
                                      [1, 0, 0, 0],
                                      [1, 0, 0, 1],
                                      [1, 0, 1, 0],
                                      [1, 0, 1, 1],
                                      [1, 1, 0, 0],
                                      [1, 1, 0, 1],
                                      [1, 1, 1, 0],
                                      [1, 1, 1, 1]], dtype=bool)

    def encode(self, data):
        pass

    def decode(self, code):
        pass


# def G(r: int, m: int):

#     if r < 0 or m < 0:
#         return
    
#     if r == 0:
#         return np.array([1 for _ in range(2**m)])
#     elif r == m:
#         return np.identity(2**m, dtype=int)

#     if r > 1:
#         return np.array([[G(r, m - 1), G(r, m - 1)], [np.zeros((r - 1, m - 1), dtype=int), G(r - 1, m - 1)]], dtype=object)
#     else:
#         return np.array([[G(r, m - 1), G(r, m - 1)], [np.zeros((1, m - 1), dtype=int), G(r - 1, m - 1)]], dtype=object)

if __name__ == '__main__':
    rm = Reed_Muller()
    print("The code is self dual: \n", 1*np.matmul(rm.G, rm.G.T))
    print("All possible codes: \n", np.array([1*np.dot(element, rm.G) for element in rm.permutations]))
