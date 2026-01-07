import hashlib
import time
class Block:
    def __init__(self,data,previous_hash):
        self.timestamp=time.time()
        self.data=data
        self.previous_hash=previous_hash
        self.hash=self.calculate_hash()
    def calculate_hash(self):
        block_string=(str(self.timestamp)+str(self.data)+str(self.previous_hash))
        return hashlib.sha256(block_string.encode()).hexdigest()
class Blockchain:
        def __init__(self):
            self.chain=[self.create_genesis_block()]
        def create_genesis_block(self):
            return Block("Genesis Block","0")
        def get_latest_block(self):
            return self.chain[-1]
        def add_block(self,new_data):
            previous_hash=self.get_latest_block().hash
            new_block=Block(new_data,previous_hash)
            self.chain.append(new_block)
            
my_blockchain=Blockchain()
my_blockchain.add_block("Block 1 Data")
my_blockchain.add_block("Block 2 Data")
my_blockchain.add_block("Block 3 Data")

for block in my_blockchain.chain:
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("-" * 40)