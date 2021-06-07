import sys
from heapq import heapify, heappush, heappop

class Node(object):
        
    def __init__(self, frequency = None, character = None):
        self.character = character
        self.frequency = frequency
        self.bit = None
        self.left = None
        self.right = None
        self.parent = None
        
    def get_frequency(self):
        return self.frequency

    def get_character(self):
        return self.character

    def has_character(self):
        return self.character != None

    def set_bit(self,bit):
        self.bit = bit

    def get_bit(self):
        return self.bit
        
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

    #Handles nodes that share the same frequencies. 
    def __lt__(self, other):
            return self.get_frequency() < other.get_frequency()

def pre_order(root_node):
    
    chars_binary_dict = dict()

    #Pre-Order Traversal
    def traverse(node, binary):

        if not node:
            return None

        #Define binary for set character
        if node.get_character():
            chars_binary_dict[node.get_character()] = [binary, node.get_frequency()]
            
        # traverse left subtree
        traverse(node.get_left_child(), binary + '0')
        
        # traverse right subtree
        traverse(node.get_right_child(), binary + '1')
    

    traverse(root_node, '')
    
    return chars_binary_dict

def huffman_encoding(data):

    
    #1. Determine frequency of each character in message
    #2. Each node can have character, frequency, left child and right child, parent, and bit (except parent).
    #3. Build a priority queue using min-heap.
    #4. More about Min-heap: https://www.askpython.com/python/examples/min-heap

    chars_frequency_dict = dict()
    heap = []

    heapify(heap)

    for c in data:
        if c in chars_frequency_dict:
            chars_frequency_dict[c] += 1 
        else:
            chars_frequency_dict[c] = 1 

    for key in chars_frequency_dict:

        node = Node(chars_frequency_dict[key],key)
        heappush(heap,(node.get_frequency(),node))



    while len(heap) != 1:

        firstPop = heappop(heap)
        secondPop = heappop(heap)
    
        parent = Node(firstPop[0] + secondPop[0])
        parent.set_left_child(firstPop[1])
        parent.set_right_child(secondPop[1])

        parent.get_left_child().set_bit('0')
        parent.get_right_child().set_bit('1')

        parent.get_left_child().set_parent(parent)
        parent.get_right_child().set_parent(parent)

        heappush(heap,(parent.get_frequency(),parent))

    

    #Recursion by DFS

    data_dictionary = pre_order(parent)

    encoded_data = ""



    for a in data:  
            encoded_data = encoded_data + (data_dictionary[a][0]) 

    # print(encoded_data)
    huffman_decoding(encoded_data,parent)





    

def huffman_decoding(data, parent):

    decoded_string = ""
    node = parent



    for c in data:

        if c is '0':
            node = node.get_left_child()
        else:
            node = node.get_right_child()

        if node.has_character():
            decoded_string = decoded_string + node.get_character()
            node = parent



    print(decoded_string)

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