
class Transaction:
    def __init__(self, name, docversion):
        self.name = name
        self.docversion = docversion

    def print_transaction(self):
        print (self.name + "::" + self.docversion)
