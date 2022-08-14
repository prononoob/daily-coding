#Notes taking program

class Notes:
    def __init__(self):
        self.items = {}
    def add(self, item):
        if item not in self.items:
            self.items[item] = False
        else:
            print(f'Item {item} already exists')
    def remove(self, item):
        pass
    def changeState(self, item):
        pass
