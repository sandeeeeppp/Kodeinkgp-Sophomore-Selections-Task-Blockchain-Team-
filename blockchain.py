import hashlib as hb
import datetime as dt


# BLOCK CLASS DEFINITION

#subtask 1
class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        # Block components
        
        self.index = index          #block no
        self.timestamp = timestamp  #time its created
        self.data = data            #transaction data(string)
        self.previous_hash = previous_hash  #link to previous block
        self.nonce = nonce          #nonce value initially 0
        self.hash = self.calculate_hash()  #it's hash id calculated by sha256

    def calculate_hash(self):
        #make a single string of all components
        block_contents = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        
        #sha256 needs bytes, not strings - hence the encoding
        raw_bytes = block_contents.encode('utf-8')
        
        # hexdigest() gives us the standard 64-character hash
        return hb.sha256(raw_bytes).hexdigest()


# BLOCKCHAIN IMPLEMENTATION

#subtask 2 
class Blockchain:
    def __init__(self):
        # Start with genesis block
        self.chain = [self.create_genesis_block()]
        # Mining difficulty (number of leading zeros required) 
        # can be changed acc to wish for particular blockchain
        self.difficulty = 4

    def create_genesis_block(self):
        # Special case for first block as it returns 0 for previous block
        return Block(0, dt.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        # Last block in the list is current head
        return self.chain[-1]

    # Simple block addition without using PoW consensus for subtask 2
    def add_block(self, data):
        prev_block = self.get_latest_block()
        new_block = Block(
            prev_block.index + 1,
            dt.datetime.now(),
            data,
            prev_block.hash
        )
        self.chain.append(new_block)
        print(f"Added block {new_block.index} directly")

    # Mining with proof-of-work(bonus)
    def mine_block(self, data):
        prev_block = self.get_latest_block()
        new_block = Block(
            prev_block.index + 1,
            dt.datetime.now(),
            data,
            prev_block.hash
        )

        print(f"Mining block {new_block.index}...")
        start_time = dt.datetime.now()
        
        #keep iterating over until we find hash with reqd threshold
        while not new_block.hash.startswith('0' * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        #the time it took to mine
        mining_time = (dt.datetime.now() - start_time).total_seconds()
        
        #appending the verified block
        self.chain.append(new_block)
        print(f"Mined block {new_block.index} in {mining_time:.2f}s")
        print(f"Hash: {new_block.hash}")
        #nonce that worked for it
        print(f"Nonce: {new_block.nonce}\n")

    #validating the chain by again computing it's hash and comparing with orignal hash and checking it's chain by comparing with previous block
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            #checking if current block's hash is still valid
            if current.hash != current.calculate_hash():
                print(f"Block {i} has been tampered with!")
                return False

            #verifying chain linkage
            if current.previous_hash != previous.hash:
                print(f"Broken link at block {i}!")
                return False

            # Bonus: Check proof-of-work requirement
            #when added with add function
            if not current.hash.startswith('0' * self.difficulty):
                print(f"Block {i} doesn't meet difficulty!")
                return False

        return True

#making a interactive CLI menu
def main_menu():
    blockchain = Blockchain()
    
    while True:
        print("\nBlockchain CLI Menu")
        print("1. Add Block with Proof-of-Work")
        print("2. Add Block Directly (No PoW)")
        print("3. View Blockchain")
        print("4. Check Validity")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            data = input("Enter block data (e.g., transaction details): ")
            blockchain.mine_block(data)
        
        elif choice == '2':
            data = input("Enter block data (e.g., transaction details): ")
            blockchain.add_block(data)
        
        elif choice == '3':
            print("\nBlockchain Contents:")
            for block in blockchain.chain:
                print(f"Block {block.index}:")
                print(f"  Timestamp: {block.timestamp}")
                print(f"  Data: {block.data}")
                print(f"  Previous Hash: {block.previous_hash}")
                print(f"  Nonce: {block.nonce}")
                print(f"  Hash: {block.hash}\n")
        
        elif choice == '4':
            if blockchain.is_valid():
                print("✓ Blockchain is valid")
            else:
                print("✗ Blockchain is INVALID!")
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main_menu()
