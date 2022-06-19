from datetime import datetime
from turtle import st

from block import Block


class Block_Chain:
    dificulty = 5
    def __init__(self):
        self.chain= self.create_root_block()
        
    def create_root_block(self):
        time = datetime.now()
        list_block = []
        list_block.append(Block(0,str(time),{"transfer":"Tuanthinh sent 1000 SHIB to Thinh37"}))
        return list_block

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def add_block(self, new_block):
        new_block.pre_hash = self.get_latest_block().hash
        new_block.hash = new_block.mine_block(Block_Chain.dificulty)
        self.chain.append(new_block)

    def check_valid(self):
        for x in range(1, len(self.chain)):
            if self.chain[x].hash != self.get_latest_block().caculate_hash():
                return False
            if self.chain[x].pre_hash != self.chain[x-1].caculate_hash():
                return False
        return True