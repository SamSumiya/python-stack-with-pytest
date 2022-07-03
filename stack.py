from typing import List


class Stack:

    def __init__(self):
        self.items: List(str) = []
        self.symbols: List(str) = []

    def show(self):
        return self.items

    def my_push(self, item):
        self.items += [item]
        return self.items

    def my_pop(self):
        popped = self.items[-1]
        self.items = self.items[:-1]
        return popped

    def my_shift(self):
        shifted = self.items[:1]
        self.items = self.items[1:]
        return shifted

    def my_unshift(self, item):
        self.items = [item] + self.items
        return self.items

    def my_peek(self):
        return self.items[-1]

    def is_empty(self):
        if self.items == []:
            return True
        return False

    def are_symbols_balanced(self):
        left_side = ['(', '[',  '{']
        right_side = [')', ']',  "}"]

        stored_left = []
        stored_right = []

        for el in self.items:
            if el in left_side:
                stored_left.append(el)
            elif el in right_side:
                stored_right.append(el)

        i = 0
        j = len(stored_right) - 1

        if len(stored_left) != len(stored_right):
            return False

        while i < len(stored_left):
            if stored_left[i] + stored_right[j] not in ['()', '[]', '{}']:
                return False
            return True
        i += 1
        j -= 1

    def length(self):
        return len(self.items)


def match_symbols(symbol_str): 
        
    symbol_bp = {
        '(' : ')', 
        '[' : ']', 
        '{' : '}',
    }
    
    openers = symbol_bp.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbol_str): 
        symbol = symbol_str[index]

        if symbol in openers: 
            my_stack.my_push(symbol)
        else:
            if my_stack.is_empty(): 
                return False
            else:
                top_item = my_stack.my_pop()
                if symbol != symbol_bp[top_item]:
                    return False
        index += 1

    if my_stack.is_empty():
        return True

    


