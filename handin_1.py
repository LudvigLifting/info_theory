import numpy as np
import math

class InfoTheory:

    def Entropy(self, P):
        
        # Input P:
        #   Matrix (2-dim array): Each row is a probability
        #       distribution, calculate its entropy,
        #   Row vector (1Xm matrix): The row is a probability
        #       distribution, calculate its entropy,
        #   Column vector (nX1 matrix): Derive the binary entropy
        #       function for each entry,
        #   Single value (1X1 matrix): Derive the binary entropy
        #       function
        # Output:
        #   array with entropies

        H = []
        h = 0
        rows, cols = np.shape(P)
        for row in range(rows):
            if cols > 1:
                H.append(-1 * sum([x * math.log2(x) if x != 0 else 0 for x in P[row]]))
            else:
                if P[row] != 0 and P[row] != 1:
                    H.append(-1 * P[row][0] * math.log2(P[row][0]) - (1 - P[row][0]) * math.log2((1 - P[row][0])))
                else:
                    H.append(0)
                
        return H

        

    def MutualInformation(self, P):
        
        # Derive the mutual information I(X;Y)
        #   Input P: P(X,Y)
        #   Output: I(X;Y)
        I = 0
        for x in range(len(P)):
            for y in range(len(P[x])):
                I += P[x][y] * math.log2(P[x][y]/(sum(P[x]) * sum([li[y] for li in P]))) if P[x][y] != 0 else 0

        return [I]


if __name__ == '__main__':

    ### init
    IT = InfoTheory()

    ### 1st test
    P1 = np.transpose(np.array([np.arange(0.0,1.1,0.25)]))# columnvector
    H1 = IT.Entropy(P1)
    print('H1 =',H1)

    ### 2nd test
    P2 = np.array([[0.3, 0.1, 0.3, 0.3],
                   [0.4, 0.3, 0.2, 0.1],
                   [0.8, 0.0, 0.2, 0.0]])
    H2 = IT.Entropy(P2)
    print('H2 =',H2)

    ### 3rd test
    P3 = np.array([[0, 3/4],[1/8, 1/8]])
    I3 = IT.MutualInformation(P3)
    print('I3 =',I3)

    ### 4th test
    P4 = np.array([[1/12, 1/6, 1/3],
                    [1/4, 0, 1/6]])
    I4 = IT.MutualInformation(P4)
    print('I4 =',I4)