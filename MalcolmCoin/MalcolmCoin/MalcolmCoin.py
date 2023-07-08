from datetime import datetime
from Block import Block
from BlockChain import BlockChain
from Transaction import Transaction
import ecdsa

MalcolmCoin = BlockChain()
girlfriendWallet = ecdsa.SigningKey.generate()
transaction = Transaction(ecdsa.SigningKey.get_verifying_key(MalcolmCoin.holderKey),ecdsa.SigningKey.get_verifying_key(girlfriendWallet), 100) 

transaction.sign(MalcolmCoin.holderKey)
MalcolmCoin.addTransaction(transaction)
MalcolmCoin.mineTransactions(ecdsa.SigningKey.get_verifying_key(MalcolmCoin.holderKey))

print(MalcolmCoin.getBalance(ecdsa.SigningKey.get_verifying_key(MalcolmCoin.holderKey)))
print(MalcolmCoin.getBalance(ecdsa.SigningKey.get_verifying_key(girlfriendWallet)))