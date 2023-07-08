import collections
from datetime import datetime
from Transaction import Transaction
from Block import Block
import ecdsa


class BlockChain:
    def __init__(self):
        self.holderKey = ecdsa.SigningKey.generate()
        self.pr = self.holderKey
        self.initalRelease = Transaction(self.holderKey, ecdsa.SigningKey.get_verifying_key(self.holderKey), 10000)
        self.chain = [ Block(datetime.today(), self.initalRelease) ]
        self.diffy = 1
        self.transactionPool = []

    def getLastBlock(self):
        return self.chain[self.chain.__len__()-1]

    def addBlock(self, block):
        block.prevHash = self.getLastBlock().hash
        block.hash = block.getHash()
        block.mine(self.diffy)
        self.diffy = self.diffy + 1
        self.chain.append(block)

    def addTransaction(self, transaction):
        if transaction.isValid(transaction, self):
            self.transactionPool.append(transaction)

    def mineTransactions(self, rewardAddress):
        rewardTrans = Transaction(ecdsa.SigningKey.get_verifying_key(self.holderKey), rewardAddress, 100)
        rewardTrans.sign(self.holderKey)
        self.addTransaction(rewardTrans)
        self.addBlock(Block(datetime.today(), self.transactionPool))

        self.transactionPool = []
    def isValid(self):
        for x in range (2, self.chain.__len__()):
            currBlock = self.chain[x]
            prevBlock = self.chain[x-1]

            if currBlock.hash != currBlock.getHash() or prevBlock.hash != currBlock.prevHash or currBlock.hasValidTrans(self):
                return False;
        return True

    def __str__(self):
        st = ""
        for x in self.chain:
            st = st+x.__str__()+"\n"

        return st

    def getBalance(self, address):
        balance = 0

        for x in self.chain:
            if isinstance(x.data, collections.abc.Sequence):
                for y in x.data:
                    if y.From == address:
                        balance = balance - y.amount

                    if y.to == address:
                        balance = balance + y.amount
            else:
                if x.data.From == address:
                    balance = balance - x.data.amount

                if x.data.to == address:
                    balance = balance + x.data.amount

        return balance

