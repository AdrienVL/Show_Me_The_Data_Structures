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

    def set_parent(self, parent):
        self.parent = parent
        
    def get_parent(self):
        return self.parent
    
    def get_right_child(self):
        return self.right

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

class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

def pre_order(tree):
    
    visit_order = list()
    
    def traverse(node):
        if node:
            # visit the node
            visit_order.append(node.get_frequency())
            
            # traverse left subtree
            traverse(node.get_left_child())
            
            # traverse right subtree
            traverse(node.get_right_child())

    # traverse(tree.get_root())
    traverse(tree)
    
    return visit_order

def huffman_encoding(data):

    #1. Determine frequency of each character in message
    #2. Each node has a character, frequency, left child and right child. 
    #3. Build a priority queue using min-heap?
    #4. More about Min-heaphttps://www.askpython.com/python/examples/min-heap


    # head = Node('c',2)
    # print(head.frequency)
    # head.increment_frequency()
    # print(head.frequency)

    #Create list fisrt
    #Convert list to nodes

    # linked_list = LinkedList()

    stringDictionary = dict()

    heap = []
    heapify(heap)

    for c in data:
        if c in stringDictionary:
            stringDictionary[c] += 1 
        else:
            stringDictionary[c] = 1 

    
    for key in stringDictionary:
        #Key is character
        #stringDic[key] is frequency
        node = Node(stringDictionary[key],key)
        heappush(heap,(node.get_frequency(),node))


    for i in heap:
        print(i)

    print('+++++++++++++')


 

    while len(heap) != 1:



        firstPop = heappop(heap)
        secondPop = heappop(heap)
    

        parent = Node(firstPop[0] + secondPop[0])
        parent.set_left_child(firstPop[1])
        parent.set_right_child(secondPop[1])




        heappush(heap,(parent.get_frequency(),parent))

       

    # print(node.get_freq uency())
    # tree = Tree(node.get_frequency())

    #Recursively Remove nodes using DFS method.
    encoded_data = ""

    # print(tree.get_root())


    # print(parent.get_left_child().get_left_child().get_left_child())

    # print(pre_order(parent))




    # return heap[0]





    

# def huffman_decoding(data,tree):
#     pass

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