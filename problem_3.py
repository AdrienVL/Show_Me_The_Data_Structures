import sys
from heapq import heapify, heappush, heappop


class Node(object):
        
    def __init__(self, frequency = None, character = None):
        self.character = character
        self.frequency = frequency
        self.huffmanCode = None
        self.left = None
        self.right = None
        self.parent = None
        self.traversed = None
        
    def get_frequency(self):
        return self.frequency
    
    def get_character(self):
        return self.character

    def set_huffmanCode(self,huffmanCode):
        self.huffmanCode = huffmanCode

    def get_huffmanCode(self):
        return self.huffmanCode
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_parent(self, parent):
        self.parent = parent
        
    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_frequency()})"
    
    def __str__(self):
        return f"Node({self.get_frequency()})"

    def __lt__(self, other):
            return self.get_frequency() < other.get_frequency()




def pre_order(tree):
    
    binaryDictionary = dict()

    def traverse(node, acc_code):
        if not node:
            return None
        if node.get_character():
            binaryDictionary[node.get_character()] = [acc_code, node.get_frequency()]
            
        # traverse left subtree
        traverse(node.get_left_child(), acc_code + '0')
        
        # traverse right subtree
        traverse(node.get_right_child(), acc_code + '1')
    

    traverse(tree, '')
    
    # return binaryDictionary
    return binaryDictionary

def huffman_encoding(data):

    #1. Determine frequency of each character in message
    #2. Each node has a character, frequency, left child and right child. 
    #3. Build a priority queue using min-heap?
    #4. More about Min-heaphttps://www.askpython.com/python/examples/min-heap



    stringDictionary = dict()
    heap = []

    heapify(heap)

    for c in data:
        if c in stringDictionary:
            stringDictionary[c] += 1 
        else:
            stringDictionary[c] = 1 

    for key in stringDictionary:

        node = Node(stringDictionary[key],key)
        heappush(heap,(node.get_frequency(),node))



    while len(heap) != 1:

        firstPop = heappop(heap)
        secondPop = heappop(heap)
    
        parent = Node(firstPop[0] + secondPop[0])
        parent.set_left_child(firstPop[1])
        parent.set_right_child(secondPop[1])

        parent.get_left_child().set_huffmanCode('0')
        parent.get_right_child().set_huffmanCode('1')

        parent.get_left_child().set_parent(parent)
        parent.get_right_child().set_parent(parent)

        # print(parent.get_left_child().get_huffmanCode())

        heappush(heap,(parent.get_frequency(),parent))

    

    #Recursion by DFS

    data_dictionary = pre_order(parent)

    encoded_data = ""



    for a in data:  
            encoded_data = encoded_data + (data_dictionary[a][0]) 



    print(encoded_data)
    huffman_decoding(encoded_data,parent)





    

def huffman_decoding(data,tree):

    decoded_string = ""

    pass

# if __name__ == "__main__":
#     codes = {}

#     a_great_sentence = "The bird is the word"

#     print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#     print ("The content of the data is: {}\n".format(a_great_sentence))

#     encoded_data, tree = huffman_encoding(a_great_sentence)

#     print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print ("The content of the encoded data is: {}\n".format(encoded_data))

#     decoded_data = huffman_decoding(encoded_data, tree)

#     print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print ("The content of the encoded data is: {}\n".format(decoded_data))

print(huffman_encoding('AAAAAAABBBCCCCCCCDDEEEEEE'))