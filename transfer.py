from datetime import datetime
import json
from block import Block
from blockchain import Block_Chain
from datetime import datetime


block1 = Block(1, str(datetime.now()),
               {"transfer": "Thinh sent 2 usdt to binance"})
block2 = Block(2, str(datetime.now()),
               {"transfer": "Thinh received 2 usdt to binance"})
block3 = Block(3, str(datetime.now()),
               {"transfer": "thinh transferred 2 usdt to shib"})

block_chain = Block_Chain()

block_chain.add_block(block1)
block_chain.add_block(block2)
block_chain.add_block(block3)
print("Before:")
for block in block_chain.chain:
    print("Block: "+str(block.index) + " \n hash: " + block.hash + "\n data transfer: " +
          json.dumps(block.data) + " \n Pre_hash: " + str(block.pre_hash)+"\n time transfer: " + str(block.timestamp))
