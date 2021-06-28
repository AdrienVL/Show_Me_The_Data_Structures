#Implementing Node 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

#Implementing Linked Lists
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    #Append node values to list

    def to_list(self):
        
        toList = []
        
        node = self.head 
        while node:
            toList.append(node.value)
            node = node.next

        
        return toList


#Union returns unique values. No duplicates.
def union(list_1, list_2):
    union_list = LinkedList()

    py_list = list_1.to_list()
    py_list2 = list_2.to_list()
    py_f_list = set(py_list + py_list2)

    for i in py_f_list:
        union_list.append(i)

    return union_list

#Intersection returns unique values. No duplicates.
def intersection(llist_1, llist_2):

    intersection_list = LinkedList()

    py_list = llist_1.to_list()
    py_list2 = llist_2.to_list()


    for i in py_list:
        intersection_list.append(i)

    return intersection_list



# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

# print (union(linked_list_3,linked_list_4))
# print (intersection(linked_list_3,linked_list_4))