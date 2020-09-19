class PCash(object):
    def __init__(self, amount=0):
        self.amount = amount

    def __str__(self):
        return f"{self.amount} PCash"


