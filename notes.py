#Notes taking program

class Notes:
    def __init__(self):
        items = {}
    def add(self, item):
        if item not in items:
            items[item] = False
        else:
            print(f'Item {item} already exists')
    def remove(self, item):
        pass
    def changeState(self, item):
        pass

