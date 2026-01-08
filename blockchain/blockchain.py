import hashlib
import time
#make a class for each block and the attributes for the block.
class Block:
    def __init__(self,data,previous_hash):
        self.timestamp=time.time() #time at which the block is created
        self.data=data #the data associated with the block;
        self.previous_hash=previous_hash #the data associated with the previous block hashed.
        self.hash=self.calculate_hash() #the data associated with the current block hashed. 
    def calculate_hash(self):
        block_string=(str(self.timestamp)+str(self.data)+str(self.previous_hash))
        return hashlib.sha256(block_string.encode()).hexdigest() #SHA-256 hashing algorithm returns a secure hash object,which is converted into a hexadecimal text that is readable
class Blockchain:
    def __init__(self):
        self.chain=[self.create_genesis_block()]#initialise the list that will hold all the individual blocks
    def create_genesis_block(self):
        return Block("Genesis Block","0")#create genesis block with data and previous hash as 0,so that the list is not empty
    def get_latest_block(self):
        return self.chain[-1]#access the last block added to the list for the previous hash
    def add_block(self,new_data):
        previous_hash=self.get_latest_block().hash #previous hash obtain
        new_block=Block(new_data,previous_hash) #creation of the new block
        self.chain.append(new_block) # add the new block to the list

my_blockchain=Blockchain() #create the block chain wiht genesis block

my_blockchain.add_block("Data 1") #create new blocks to be added to the blockchain 
my_blockchain.add_block("Data 2")
my_blockchain.add_block("Data 3")

for block in my_blockchain.chain: #print the all blocks attributes of the blocks in the blockchain
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print( )
    

