import numpy as np
import random

class Reed_Muller:

    def __init__(self):

        self.codewords = []
        self.syndrome = np.array([])
        self.G = np.array([[1, 0, 1, 0, 1, 0, 1, 0],
                           [0, 1, 0, 1, 0, 1, 0, 1],
                           [0, 0, 1, 1, 0, 0, 1, 1],
                           [0, 0, 0, 0, 1, 1, 1, 1]], dtype=bool)
        
        possible_data = np.array([[int(char) for char in f"{i:04b}"] for i in range(2**4)], dtype=bool)

        codewords = []
        for data in possible_data:
            codeword = np.matmul(data, self.G, dtype=int) % 2
            codewords.append(codeword)
        self.codewords = np.array(codewords)

    def minimum_distance(self) -> int:
        
        dist = 999999
        for i, codeword in enumerate(self.codewords):
            for comp in self.codewords[i + 1:]:
                result = [codeword[e] ^ comp[e] for e in range(8)]
                if sum(result) < dist:
                    dist = sum(result)
        
        return dist
    
    def encode(self, data):

        assert len(data) <= 4
        return np.matmul(data, self.G, dtype=int) % 2

    def decode(self, code, syndrome):

        #Calculate syndrome vector
        s_vector = np.matmul(self.G, code, dtype=int) % 2

        if sum(s_vector) != 0:
            #error exists
            pos = -1
            for i, sub in enumerate(syndrome):
                if np.array_equal(sub, s_vector):
                    pos = i
                    break
                    
            #Correct error 
            code[pos] = code[pos] ^ 1
            print(f"Error detected and corrected: {code}")

        #Decode the codeword
        for i, codeword in enumerate(self.codewords):
            if np.array_equal(codeword, code):
                message = np.array([int(char) for char in f"{i:04b}"])
                break

        return message

    def flip(self, code):
        
        rand = random.randint(0, len(code) - 1)
        code[rand] = code[rand] ^ 1
        return code


if __name__ == '__main__':

    rm = Reed_Muller()
    
    print("\nMinimum distance = ", rm.minimum_distance())
    
    g_gt = np.matmul(rm.G, rm.G.T, dtype=int) % 2
    print("\nG * G^T = 0: {}".format(0 == np.sum(np.ravel(g_gt))))
    print(g_gt)
    
    all_messages = np.array([[int(char) for char in f"{i:04b}"] for i in range(2**4)], dtype=int)
    
    print("\nAll possible messages with corresponding codeword:\nMessage -> codeword")
    for message in all_messages:
        print("{} -> {}".format("".join(str(message)), rm.encode(message)))
    
    print("\nSyndrome vectors for all possible one bit faults:\nFault -> Syndrome vector")
    syndrome = []
    i = int(2**7)
    while i > 0:
        arr = np.array([int(char) for char in f"{i:08b}"], dtype=int)
        s_vector = np.matmul(rm.G, arr) % 2
        syndrome.append(s_vector)
        print(f"{arr} -> {s_vector}" )
        i = i >> 1
    syndrome = np.array(syndrome)

    print("\nEncoding and decoding:")
    message = all_messages[random.randint(0, len(all_messages) - 1)]
    print(f"Message to send is: {message}")
    encoded = rm.encode(message)
    print(f"Encoded message: {encoded}")
    print(f"Decode original code: {rm.decode(encoded, syndrome)}\n")
    rm.flip(encoded)
    print(f"Flip one random bit: {encoded}")
    print(f"Decode altered code: {rm.decode(encoded, syndrome)}")
