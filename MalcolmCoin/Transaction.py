import ecdsa

class Transaction:
    def __init__(self, frm, to, amount):
        self.From = frm
        self.to = to
        self.amount = amount

    def __str__(self):
        return "From: "+self.From.__str__() + " To: "+ self.to.__str__() + " Amount: " + self.amount.__str__()

    def sign(self, pk):
        if ecdsa.SigningKey.get_verifying_key(pk) == self.From:
            self.signature = pk.sign((self.From.__str__() + self.to.__str__() + self.amount.__str__()).encode("utf-8"))

    def isValid(self, tx, chain):
        return tx.From is not None and tx.to is not None and tx.amount is not None and chain.getBalance(tx.From) >= tx.amount and self.From.verify(tx.signature, (self.From.__str__() + self.to.__str__() + self.amount.__str__()).encode("utf-8"))