import math
import os
import numpy as np

def char_counter(file):
    
    counts = {}
    for line in file:
        for char in line:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
                
    total_chars = sum([item[1] for item in counts.items()])

    #Sort in descending probability
    counts = {k:v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
    for key in counts:
        counts[key] /= total_chars

    return counts

def Entropy(P: list):
            
    return (-1 * sum([x * math.log2(x) if x != 0 else 0 for x in P]))

def Code_tree(counts: dict):
    
    tree = {}
    counter = 1
    for key in counts.keys():
        if counter > 1 and counts[key] <
        tree[key] = bin(counter)
        counter += 1


if __name__ == '__main__':

    with open(os.path.join(os.sys.path[0], "Alice29.txt"), "r") as file:
        counts = char_counter(file)

    print([item[1] for item in counts.items()])
    H = Entropy([item[1] for item in counts.items()])
    print("Entropy H = {} (Optimal bit/symbol)".format(H))