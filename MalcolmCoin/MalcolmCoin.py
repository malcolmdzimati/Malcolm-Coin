from datetime import datetime
from Block import Block
from BlockChain import BlockChain
from Transaction import Transaction
import ecdsa

MalcolmCoin = BlockChain()
girlfriendWallet = ecdsa.SigningKey.generate()
thirdNigga = ecdsa.SigningKey.generate()
print("Welcome to Malcolm Coin:\n")

print("Malcolm Balance: "+MalcolmCoin.getBalance(ecdsa.SigningKey.get_verifying_key(MalcolmCoin.holderKey)).__str__())
print("Lali Balance: "+MalcolmCoin.getBalance(ecdsa.SigningKey.get_verifying_key(girlfriendWallet)).__str__())
print("Anonymous Nigga: "+MalcolmCoin.getBalance(ecdsa.SigningKey.get_verifying_key(thirdNigga)).__str__())

print("\nMalcolm Sending 2000 Malcolm Coins to Lali")
transaction = Transaction(ecdsa.SigningKey.get_verifying_key(MalcolmCoin.holderKey),ecdsa.SigningKey.get_verifying_key(girlfriendWallet), 2000)

transaction.sign(MalcolmCoin.holderKey)
MalcolmCoin.addTransaction(transaction)
MalcolmCoin.mineTransactions(ecdsa.SigningKey.get_verifying_key(thirdNigga))
print("Anonymous Nigga mined the transaction: rewarded with 100 Malcolm coins\n")

print("Malcolm Balance: "+MalcolmCoin.getBalance(ecdsa.SigningKey.get_verifying_key(MalcolmCoin.holderKey)).__str__())
print("Lali Balance: "+MalcolmCoin.getBalance(ecdsa.SigningKey.get_verifying_key(girlfriendWallet)).__str__())
print("Anonymous Nigga: "+MalcolmCoin.getBalance(ecdsa.SigningKey.get_verifying_key(thirdNigga)).__str__())

print("\nLali Sending 500 Malcolm Coins to Malcolm")
transaction2 = Transaction(ecdsa.SigningKey.get_verifying_key(girlfriendWallet), ecdsa.SigningKey.get_verifying_key(MalcolmCoin.holderKey), 500)

transaction2.sign(girlfriendWallet)
MalcolmCoin.addTransaction(transaction2)
MalcolmCoin.mineTransactions(ecdsa.SigningKey.get_verifying_key(thirdNigga))
print("Anonymous Nigga mined the transaction: rewarded with 100 Malcolm coins\n")

print("Malcolm Balance: "+MalcolmCoin.getBalance(ecdsa.SigningKey.get_verifying_key(MalcolmCoin.holderKey)).__str__())
print("Lali Balance: "+MalcolmCoin.getBalance(ecdsa.SigningKey.get_verifying_key(girlfriendWallet)).__str__())
print("Anonymous Nigga: "+MalcolmCoin.getBalance(ecdsa.SigningKey.get_verifying_key(thirdNigga)).__str__())