# Minimal Blockchain Implementation for KodeinKGP Sophomore Selections Task

## In the block class:
- **Index:** Refers to the position of that particular block in the blockchain
- **Timestamp:** Records the Date and time of transaction in block
- **Data:** It's the transaction record string (for eg:"Raju gave 0.2 BTC to Bheem")
- **Previous Hash:** Each block records previous block hash as a way to link them together hence forming blockchain
- **Nonce:** A integer value that is used to generate different hash ids required by the difficulty threshold
- **Hash:** It's the unique ID associated with a particular block depending on each of it's component generated using SHA-256 algorithm

## In the Blockchain Class (core logic):
- First genesis block(first block) is created by `create_genesis_block()` function and assigned 0 to prev hash id
- `get_return_block()` function returns te index of last chain to be used by other functions
- Blocks can be added in two ways:
    - `add_block()`: This is a simple and direct method to add block without using any consensus mechanism.
    - `mine_block()`: This way relies on Proof of Work consensus and adds a block only after it satisfies a threshold
- The chain is linked together bby using prev hashes, each block stores it's prev bloc hash (kind of reverse linked list logic)

## Validation Logic:
- **Hash Correctness:** We compute hash for every block and check if it's matching the Hash Id written inside the block
- **Proper linkage:** We check if the block is linking to the block that is listed in previous_hash by checking in the index i-1 hash for ith block and check if both are same

## Proof-of-Work:
- **Difficulty:** It is set to 4 (I didn't think of any special reasons, just a number that has reasonable computing time)
- **Nonce:** It is a int value in block that can be changed over to find a different hash ID
- **Mining the blocks:** The blocks are mined by iterating the nonce from 0 to a value that satsisfies the threshold condition (like hash id leading with 4 zeroes)

## Requirements:
- Python 3.6 or higher version
- No external libraries are needed

## Running the script:
- Save the code in a file 
- Open a terminal or command prompt and type out these:
    ```
    cd path/to/your/folder
    python blockchain.py
    ```

## After running you'll see something like this: 
 
    Blockchain CLI Menu
    1. Add Block with Proof-of-Work
    2. Add Block Directly (No PoW)
    3. View Blockchain
    4. Check Validity
    5. Exit
    Enter your choice (1-5):


    
        
