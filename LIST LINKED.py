class Linkedlist:
    def __init__(self):
        self.head=None

    def add_at_front(self,Data):
        self.head=Node(Data,self.head)
    def add_at_end(self,data):
        if not self.head:
            self.head=Node(Data,None)
             return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=Node(Data,None)
    