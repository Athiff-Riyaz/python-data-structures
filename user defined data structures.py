"""
some of the most popular data structures are:
-stacks
-Queues
-Linked lists
-Graphs
we use the above data structures and use them to solve popular problems."""
#stacks
"""
Terminology
-Adding a new element onto the stack is called push.
-Removing an element from the stacks is called pop.

Applications
stacks can be used to create undo-redo functionalities,parsing expressions
(inflix to postfix/prefix conversion), and much more."""
class stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self, item):
        self.items.insert(0, item)
    def pop(self):
        return self.items.pop(0)
    def print_stack(self):
        print(self.items)