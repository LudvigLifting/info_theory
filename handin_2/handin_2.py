import math
import os
from operator import attrgetter

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
    #print(counts)
    for key in counts:
        counts[key] /= total_chars

    return counts

def Entropy(P: list):
            
    return (-1 * sum([x * math.log2(x) if x != 0 else 0 for x in P]))

def print_tree(node, level=0, counter=0):
    if node != None:
        print_tree(node.left, level + 1, counter)
        print(' ' * 4 * level + '-> ' + str(node.value))
        print_tree(node.right, level + 1, counter)

def code_tree(probs: list):

    katt = False
    if len(probs) < 2:
        return probs.pop()
        
    prob_0 = probs.pop()
    prob_1 = probs.pop()
    node = Node((prob_0.value[0] + prob_1.value[0], prob_0.value[1] + prob_1.value[1]))
    node.right, node.left = (prob_1, prob_0) if prob_1.value[1] > prob_0.value[1] else (prob_0, prob_1)

    length = len(probs)

    #Insert new node in the right place
    if length > 0:
        for index, item in enumerate(probs):
            if katt:
                print("item = {}, value = {}".format(item.value[1], node.value[1]))
            if item.value[1] < node.value[1]:
                if index == length - 1:
                    probs.append(node)
                    break
                probs.insert(index, node)
                break
            if index == length - 1:
                    probs.append(node)
            
    else:
        probs.append(node)
    
    return code_tree(probs)

def print_leaves(root: Node, counter: int=0) -> int:

    if not root:
        return counter

    if not root.left and not root.right:
        print(root.value)
    
    if root.left:
        counter = print_leaves(root.left, counter)

    if root.right:
        counter = print_leaves(root.right, counter)

def assign_codes(root: Node, code_map: dict={}, code: str="") -> None:
    
    if not root:
        return

    if not root.left and not root.right:
        code_map[root.value[0]] = code
    
    if root.left:
        code += "0"
        assign_codes(root.left, code_map, code)

    if root.right:
        code += "1"
        assign_codes(root.right, code_map, code,)

if __name__ == '__main__':

    with open(os.path.join(os.sys.path[0], "Alice29.txt"), "r") as file:
        counts = char_counter(file)
    #print("Length of counts = ", len(counts))
    root = code_tree([Node(val) for val in list(counts.items())])

    mapping = {}
    assign_codes(root, mapping)

    sorted_map = sorted(mapping.items(), key=lambda item: item[0])
    sorted_counts = sorted(counts.items(), key=lambda item: item[0])
    
    print("\nDistribution of letters: \n")
    for entry in sorted_counts:
        print("Character: \"{}\", probability: {}".format(entry[0], entry[1]))

    coded_text = ""
    counter = 0
    with open(os.path.join(os.sys.path[0], "Alice29.txt"), "r") as file:
        for line in file:
            for char in line:
                counter += 1
                if char in mapping.keys():
                    coded_text += mapping[char]
                else:
                    print("Missing mapping: ", char)

    print("\nCode table: \n")
    for entry in sorted_map:
        print("Character: \"{}\", code: {}".format(entry[0], entry[1]))
    
    print("\nLength of the uncoded text = ", counter*8)
    print("Length of the coded text = ", len(coded_text))

    entropy_uncoded = Entropy([prob for prob in list(counts.values())])
    print("Entropy of text file = ", entropy_uncoded)
 
    average_code_len = 0
    for index, e in enumerate(list(map(len, [i[1] for i in sorted_map]))):
        print(sorted_counts[index][1])
        average_code_len += e*sorted_counts[index][1]
        
    print("Average code length = ", average_code_len)
    #print(coded_text)
    #print(print_leaves(root))