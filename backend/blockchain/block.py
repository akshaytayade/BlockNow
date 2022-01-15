import time

from backend.util.crypto_hash import crypto_hash


GENESIS_DATA = {
    'timestamp':1,
    'last_hash':'genesis_last_hash',
    'hash':'genesis_hash',
    'data': [],
    'difficulty':3,
    'nonce':'gensis_nonce'
}

class Block:
    def __init__(self,timestamp, last_hash, hash, data, difficulty, nonce):
        self.data = data
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return(
            'Block('
            f'timestamp: {self.timestamp},'  
            f'last_hash: {self.last_hash},'
            f'hash: {self.hash},'
            f'hash: {self.data}),'
            f'difficulty:{self.difficulty},'
            f'nonce:{self.nonce})'
        )

    @staticmethod
    def mine_block(last_block,data):
        '''mine till block hash meets the leading work'''
        timestamp = time.time_ns()
        last_hash =last_block.hash
        difficulty= last_block.difficulty
        nonce=0
        hash=crypto_hash(timestamp,last_hash,data,difficulty,nonce)

        while hash[0:difficulty] != '0'*difficulty:
            nonce+=1
            timestamp = time.time_ns()
            hash=crypto_hash(timestamp,last_hash,data,difficulty,nonce)


        return Block(timestamp,last_hash,hash,data,difficulty,nonce)

    @staticmethod
    def genesis():
        # return Block(
        #     timestamp= GENESIS_DATA['timestamp'],
        #     last_hash=GENESIS_DATA['last_hash'],
        #     hash=GENESIS_DATA['hash'],
        #     data=GENESIS_DATA['data']
        #     )
        return Block(**GENESIS_DATA)

def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block,'foo')
    print(block)


if __name__ == '__main__':
    main()