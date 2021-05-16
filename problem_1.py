# After removing an element, we use the put()
#All operations must take O(1) time
# Implement Queue - Linked Lists
import queue


class LRU_Cache(object):

    

    def __init__(self, capacity):
        # Initialize class variables
        self.dictionary = dict()
        self.q = queue.Queue()
        self.capacity = capacity
        self.q_size = 0
        
        
    

    def get(self, key):

        self.q.get() #Get oldest item and removes it from queue


        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.dictionary.get(key) is None:
            return -1
        else:
            return self.dictionary.get(key)

    
    #Insert key values in Queue.
    #Update existing dictionary with key value set from queue

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.


        #Insert newest element to queue

        new_set = {key:value}
        self.q.put(key)
        self.q_size += 1

        

        if  self.q_size==self.capacity:
            oldest_element_key = self.q.get() #Get oldest item and removes it fromq queue
            #Remove element key from dictionary
            self.dictionary.pop(oldest_element_key)
            #and update dictionary with new key value pair
            self.dictionary.update(new_set)
            
        else:

            self.dictionary.update(new_set)


        
        

our_cache = LRU_Cache(5)



our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.dictionary)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print(our_cache.dictionary)