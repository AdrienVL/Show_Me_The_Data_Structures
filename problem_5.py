import hashlib
import datetime



class Block:

    def __init__(self, timestamp, data, previous_hash = 0):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None

    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = repr(self).encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

    def __repr__(self):
      #   return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(" | ") + str(self.hash)
        return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(" | ") 


class BlockChain:
      def __init__(self):
            self.head = None

      
      def append(self,timestamp, data):
            if self.head is None:
                  self.head = Block(timestamp, data)
                  return
            
            
            block = self.head
            previous_hash = block.hash

            while block.next:
                  block = block.next
                  previous_hash = block.hash
            block.next = Block(timestamp, data, previous_hash)
            return

      def to_list(self):
        
        toList = []
        
        block = self.head 
        while block:
            toList.append(block.hash)
            print(repr(block))
            block = block.next
        
        return toList



blockchain = BlockChain()
blockchain.append(datetime.datetime.now(), "First")
blockchain.append(datetime.datetime.now(), "Second")
blockchain.append(datetime.datetime.now(), "Third")

print(blockchain.to_list())





