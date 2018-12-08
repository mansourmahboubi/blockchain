from random import randrange
from datetime import datetime
from hashlib import sha256


class Block:
    def __init__(self, previous_block_hash, data, timestamp):
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.generate_hash()

    def generate_hash(self):
        header_bin = (str(self.previous_block_hash) + str(self.data) + str(self.timestamp))

        inner_hash = sha256(header_bin.encode()).hexdigest().encode()
        outer_hash = sha256(inner_hash).hexdigest()
        return outer_hash

    def __str__(self):
        return self.hash


class Blockchain:
    def __init__(self, number_of_blocks):
        self.blockchain = []
        self.number_of_blocks = number_of_blocks
        self.create_genesis_block()
        self.create_block_chain()

    def create_genesis_block(self):
        genesis_block = Block("0", "0", datetime.now())
        self.blockchain.append(genesis_block)
        print("The genesis block has been created.")
        print("Hash: %s" % self.blockchain[0].hash)

    def create_block_chain(self):
        for i in range(1, self.number_of_blocks):
            self.blockchain.append(Block(self.blockchain[i-1].hash,
                                         randrange(100, 1000),
                                         datetime.now()))

    def __str__(self):
        for i in range(1, self.number_of_blocks):
            print("Block #%d created." % i, "\nHash: %s" % self.blockchain[i].hash)
        return ""


if __name__ == '__main__':
    number_of_blocks = 10
    blockchain = Blockchain(number_of_blocks)
    print(blockchain)
