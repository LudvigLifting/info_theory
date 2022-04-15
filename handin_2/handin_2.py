import math
import os
import numpy as np

class Node:
    def __init__(self, value, left=None, right=None):
      self.left = left
      self.right = right
      self.value = value



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

def print_tree(node, level=0, counter=0):
    if node != None:
        print_tree(node.left, level + 1, counter)
        print(' ' * 4 * level + '-> ' + str(node.value[1]))
        print_tree(node.right, level + 1, counter)

def Code_tree(probs: list, node: Node = None):
    
    if len(probs) > 1:
        
        prob_0 = probs.pop()
        prob_1 = probs.pop()
        node = Node((prob_0[0] + prob_1[0], prob_0[1] + prob_1[1]))
        node.right, node.left = (Node(prob_1), Node(prob_0)) if prob_1[1] > prob_0[1] else (Node(prob_0), Node(prob_1))

        probs.append(node.value)
        probs = sorted(probs, key=lambda item: item[1], reverse=True)
        node, probs = Code_tree(probs, node)

    return node, probs

if __name__ == '__main__':

    with open(os.path.join(os.sys.path[0], "Alice29.txt"), "r") as file:
        counts = char_counter(file)
    
    H = Entropy([item[1] for item in counts.items()])
    #print("Entropy H = {} (Optimal bit/symbol)".format(H))
    tree = Code_tree(list(counts.items()))[0]
    print("Value = {}, \nleft = {}, \nright = {}".format(tree.value, tree.left.left.value[1], tree.right.value[1]))
    print_tree(tree)