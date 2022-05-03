import math

class HuffmanCoding: 

    def __init__(self, text): 
        self.codewords = {}         # symbols -> codewords 
        self.text = text

        self.symbolToProb = {}      # symbols -> probability 
        self.probToSymbol = {}      # probability -> symbols
        self.innerNodes = []        # list containing all inner nodes(probabilities) of the Huffman tree 

        self.huffmanTree = []       


    def getProbabilityDistribution(self): 
        total_nbr_symbols = len(text)

        for symbol in self.text: 
            if symbol in self.symbolToProb: 
                self.symbolToProb[symbol] = self.symbolToProb[symbol] + 1
            else: 
                self.symbolToProb[symbol] = 1

        for symbol in self.symbolToProb: 
            occ = self.symbolToProb[symbol]

            self.symbolToProb[symbol] = occ/total_nbr_symbols  
            self.probToSymbol[occ/total_nbr_symbols] = symbol
            self.huffmanTree.append(HuffmanNode(occ/total_nbr_symbols, self.probToSymbol[occ/total_nbr_symbols], None, None))

        return self.probToSymbol

    
    def findCodes(self): 
    
        self.huffmanTree.sort(key=lambda node:node.prob)

        while len(self.huffmanTree) > 2: 

            nodeOne = self.huffmanTree[0]
            nodeTwo = self.huffmanTree[1]

            newNode = HuffmanNode(nodeOne.prob+nodeTwo.prob, None, nodeOne, nodeTwo)
            self.innerNodes.append(newNode.prob)

            self.huffmanTree = self.huffmanTree[1:len(self.huffmanTree)]
            self.huffmanTree[0] = newNode

            self.huffmanTree.sort(key=lambda node:node.prob)
            print("Node value: {}, node.right: {}, node.left: {}".format(newNode.prob, newNode.right.prob, newNode.left.prob))
        
        nodeOne = self.huffmanTree[0]
        nodeTwo = self.huffmanTree[1]
        rootNode = HuffmanNode(nodeOne.prob+nodeTwo.prob, None, nodeOne, nodeTwo)
        self.innerNodes.append(rootNode.prob)

        codeword = ""
        self.constructCodewords(rootNode, codeword)


    def constructCodewords(self, node, codeword): 
        
        if node is None: 
            return 

        if node.isLeaf(): 
            self.codewords[node.symbol] = codeword
            codeword = ""

        self.constructCodewords(node.left, codeword + "0")
        self.constructCodewords(node.right, codeword + "1")

        codeword = codeword[0:len(codeword)-1]

    
    def Compress(self, text): 
        compressedText = ""

        for symbol in text: 
            compressedText = compressedText + self.codewords[symbol]

        return len(compressedText)


    def getCodewords(self): 
        return self.codewords


    # Utilizing path length lemma to determine the average codeword length 
    def getAverageCodewordLength(self): 
        codewordLength = 0

        for prob in self.innerNodes:
            codewordLength += prob

        return codewordLength


    def calculateEntropy(self): 
        H = 0

        for prob in self.probToSymbol: 
            if prob != 0: 
                H += prob*math.log2(prob)

        return -H 


class HuffmanNode: 

    def __init__(self, prob, symbol, left, right):
        self.left = left 
        self.right = right 
        self.prob = prob
        self.symbol = symbol 

    def isLeaf(self): 
        return self.left is None and self.right is None


if __name__ == '__main__':

    file = open("Alice29.txt", "r")
    text = file.read()
    
    huffman = HuffmanCoding(text)

    distribution = huffman.getProbabilityDistribution()
    huffman.findCodes()
    compressedText = huffman.Compress(text)
    codewords = huffman.getCodewords()
    averageCodewordLength = huffman.getAverageCodewordLength()
    entropy = huffman.calculateEntropy()


    #####################################################################

    # for symbol in distribution: 
    #     print("Symbol is: {0}, probability is: {1}".format(symbol, distribution[symbol]))

    # for symbol in codewords: 
    #     print("Symbol is: {0}, codeword is: {1}".format(symbol, codewords[symbol]))

    #distribution.sort(key=distribution.keys(), reverse=True)

    for prob in sorted(distribution): 
        print(" {0} & {1} & {2} \\\\".format(distribution[prob], prob, codewords[distribution[prob]]))

    print("Length of text is: ", len(text)*7) # since ASCII-representation is 7 bits per symbol
    print("Length of compressed text is: ", compressedText)
    print("Average codeword length is: ", averageCodewordLength)
    print("Entropy of the distribution is: ", entropy)
