import collections

class LRU_Cache(object):

    

    ''' Initialize class variables
    '''
    def __init__(self, capacity):
        #Cache as dictionary
        self.dictionary = dict()
        #Track recently used entry with queue
        self.q = collections.deque([],maxlen=capacity)
        self.capacity = capacity
        self.q_size = 0
    
    def get(self, key):

        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.dictionary.get(key) is None:
            return -1
        else:
            oldest_element_key = self.q.popleft() #Records oldest item and remove it from queue
            #Re-insert oldest item to queue, as most recentently called upon item
            self.q.append(oldest_element_key)
            return self.dictionary.get(key)

    def set(self, key, value):

        #Insert newest key to queue
        new_set = {key:value}
        self.q.append(key)
        #Track q size
        self.q_size += 1

        #Cache memory has reached its limit.
        if  self.q_size==self.capacity:
            oldest_element_key = self.q.popleft() #Recoreds oldest item and remove it from queue
            #Remove element key from dictionary
            self.dictionary.pop(oldest_element_key)
            #and update dictionary with new key value pair (Merging new_set, a dictionary with self.dictionary)
            self.dictionary.update(new_set)
            
        else:

            self.dictionary.update(new_set)


#Test Cases

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