import os, time

#Model

class Notes:

    def __init__(self):
        self.items = {}
        print('Model initialised!')

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

    def show(self):
        for item in self.items:
            if self.items[item] == True:
                y = '[X]'
            else:
                y = '[ ]'
            x = y + item
            print(x)

#View

class viewNotes:

    def __init__(self):
        os.system('clear')
        print('View initialized!')

    def clItems(self):
        os.system('clear')
        f.show()

#Controller

class controllNotes:

    def __init__(self):
        global f, v
        f, v = Notes(), viewNotes()
        print('Controller initialized!')

    def add(self, item):
        f.add(item)
        v.clItems()

    def remove(self, item):
        f.remove(item)
        v.clItems()

    def tick(self, item):
        f.changeState(item)
        v.clItems()


