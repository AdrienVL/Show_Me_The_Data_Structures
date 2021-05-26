import sys
from heapq import heapify, heappush, heappop

# class childNode:
#     def __init__(self, character, frequency):
#         self.character = character
#         self.frequency = frequency

        
# class internalNode:
#     def __init__(self, frequency):
#         self.frequency = frequency
#         self.left = None
#         self.right = None

#     def set_left_child(self,left):
#         self.left = left
        
#     def set_right_child(self, right):
#         self.right = right
        
#     def get_left_child(self):
#         return self.left

#     def get_right_child(self):
#         return self.right

    # def set_frequency(self,frequency):
    #     self.frequency = frequency
        
    # def get_frequency(self):
    #     return self.frequency

class Node(object):
        
    def __init__(self, frequency = None, character = None):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None
        self.parent = None
        
    def get_frequency(self):
        return self.frequency
    
    def get_character(self):
        return self.character
        
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
        node = Node(stringDictionary[key],key)
        heappush(heap,(node.get_frequency(),node.get_character()))


    for i in heap:
        print(i)

    print('+++++++++++++')




    node = None    

    while len(heap) != 1:
        firstPop = heappop(heap)
        secondPop = heappop(heap)

        # print(firstPop[1])

        if node is None:
            node = Node(firstPop[0]+secondPop[0])
        else:
            node.set_parent(Node(firstPop[0]+secondPop[0]))
            node = node.get_parent() 

        print(node)
        if firstPop[0] <= secondPop[0]:
            node.set_left_child(Node(firstPop[0],firstPop[1]))
            node.set_right_child(Node(secondPop[0],secondPop[1]))
        else:
            node.set_right_child(Node(firstPop[0],firstPop[1]))
            node.set_left_child(Node(secondPop[0],secondPop[1]))

        heappush(heap,(node.get_frequency(),node.get_character()))



    # print(node.get_left_child())



    return heap[0]





    

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