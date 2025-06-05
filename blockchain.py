import hashlib as hb
import datetime as dt

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hb.sha256(block_string.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
    
    #I was originally going to use time.time() here, but switched to datetime for readability

    def create_genesis_block(self):
        return Block(0, dt.datetime.now(), "Genesis Block", "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, data):
        prev_block = self.get_latest_block()
        new_block = Block(
            prev_block.index + 1,
            dt.datetime.now(),
            data,
            prev_block.hash
        )
        self.chain.append(new_block)
        print(f"Block added directly: {new_block.hash}")
    
    def mine_block(self, data):
        prev_block = self.get_latest_block()
        new_block = Block(
            prev_block.index + 1,
            dt.datetime.now(),
            data,
            prev_block.hash
        )
        
        print(f"Mining block with difficulty {self.difficulty}...")
        start_time = dt.datetime.now()
        
        while not new_block.hash.startswith('0' * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()
        
        #thought I should output mining time so I could refine mining technique with other approach in future
        mining_time = (dt.datetime.now() - start_time).total_seconds()
        self.chain.append(new_block)
        print(f"Block mined in {mining_time:.2f}s: {new_block.hash}")
        print(f"Nonce used: {new_block.nonce}\n")

    #can also take nonce timestamp method as nonce as int would run out soon in practical sense but I kept it simple
    
    def is_valid(self):
        # Check genesis block's hash 
        genesis = self.chain[0]
        if genesis.hash != genesis.calculate_hash():
            print("Genesis block tampered!")
            return False
        # checking for further blocks in linkage
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
        #could've added a starting zero filter to check for blocks appended through add fn
        return True

#made simple CLI method just to check blockchain's working
def main_menu():
    blockchain = Blockchain()
    
    while True:
        #basic menu to choose from
        print("\nBlockchain CLI Menu")
        print("1. Add Block with Proof-of-Work")
        print("2. Add Block Directly (No PoW)")
        print("3. View Blockchain")
        print("4. Check Validity")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        #bonus: PoW method
        if choice == '1':
            data = input("Enter block data (e.g., transaction details): ")
            blockchain.mine_block(data)
        
        #for direct adding method
        elif choice == '2':
            data = input("Enter block data (e.g., transaction details): ")
            blockchain.add_block(data)
        
        #viewing the whole blockchain
        #future improvement could be to look at individual blockwise

        elif choice == '3':
            print("\nBlockchain Contents:")
            for block in blockchain.chain:
                print(f"Block {block.index}:")
                print(f"  Timestamp: {block.timestamp}")
                print(f"  Data: {block.data}")
                print(f"  Previous Hash: {block.previous_hash}")
                print(f"  Nonce: {block.nonce}")
                print(f"  Hash: {block.hash}\n")
        
        #checking the chain
        elif choice == '4':
            if blockchain.is_valid():
                print("✓ Blockchain is valid")
            else:
                print("✗ Blockchain is INVALID!")
        
        #exiting program 
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main_menu()
