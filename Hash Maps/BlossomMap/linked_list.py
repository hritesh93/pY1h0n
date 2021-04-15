class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def get_value(self):
        return self.value
  
    def get_next_node(self):
        return self.next_node
  
    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node
  
    def insert(self, new_node):
        current_node = self.head_node

        if not current_node:
            self.head_node = new_node

        while(current_node):
            next_node = current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(new_node)
            current_node = next_node

    def __iter__(self):
        current_node = self.head_node
        while(current_node):
            yield current_node.get_value()
            # yield is used to return from a function without destroying the states of its local variable.
            # When the function is called, the execution starts from the last yield statement.
            # Any function that contains a yield keyword is termed as generator. Hence, yield is what makes a generator
            current_node = current_node.get_next_node()
