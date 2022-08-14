#Notes taking program

class Notes:
    def __init__(self):
        self.items = {}
        print('Script initialised!')
    def add(self, item):
        if item not in self.items:
            self.items[item] = False
        else:
            print(f'Item {item} already exists')
    def remove(self, item):
        if item in self.items:
            self.items.pop(item)
        else:
            print(f'Item {item} doesn\'t exist')
    def changeState(self, item):
        if item in self.items:
            self.items[item] = not self.items[item]
        else:
            print(f'Item {item} doesn\'t exist')
