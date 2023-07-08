from ctypes import Array
import hashlib

class Block:
    def __init__(self, timestamp, data):
        self.timeStamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        self.data = data
        self.prevHash = ""
        self.nonce = 0
        self.hash = self.getHash()

    def hasValidTrans(self, chain):
        for x in self.data:
            if not x.isValid(x, chain):
                return False
        return True

    def getHash(self):
        return hashlib.sha256((self.prevHash + self.timeStamp + self.data.__str__()+ self.nonce.__str__()).encode('utf-8')).hexdigest()

    def mine(self, diff):
        di = ""
        for x in range(diff):
            di = di + "0"

        while self.hash.endswith(di):
            self.nonce = self.nonce + 1
            self.hash = self.getHash()

    def __str__(self):
        return " " + self.data.__str__() + " nonce: " + self.nonce.__str__() + " Hash: " + self.prevHash + " Date: " + self.timeStamp
