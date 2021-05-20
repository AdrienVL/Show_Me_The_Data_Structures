import sys
import heapq

class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, character, frequency):
        if self.head is None:
            self.head = Node(character,frequency)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(character,frequency)
        return



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

    linked_list = LinkedList()

    stringDictionary = dict()

    for c in data:
        if c in stringDictionary:
            stringDictionary[c] += 1 
        else:
            stringDictionary[c] = 1 

    
    for key in stringDictionary:
        linked_list.append(key,stringDictionary[key])

    node = linked_list.head

    while node:
        print(node.frequency)
        node = node.next





    

def huffman_decoding(data,tree):
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