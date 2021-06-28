class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


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

    def to_list(self):
        
        toList = []
        
        node = self.head 
        while node:
            toList.append(node.value)
            node = node.next

        
        return toList



def common_elements(llist_1, llist_2):

    a = [5, 10, 15, 20, 25, 30]
    b = [10, 20, 30, 40, 50, 60]

    print(a)
    print(b)
    common_list = [c for c in a if c in b]
    print(common_list)

        
    py_list = llist_1.to_list()
    py_list2 = llist_2.to_list()

    print(py_list)
    print(py_list2)

    cc = [c for c in py_list if c in py_list2]
    return cc


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [5, 10, 15, 20, 25, 30]
element_2 = [10, 20, 30, 40, 50, 60]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print (use_case(linked_list_1,linked_list_2))

