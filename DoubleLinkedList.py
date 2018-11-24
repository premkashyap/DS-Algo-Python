from SinglyLinkedList import SinglyLinkedListNode, SinglyLinkedList

class DoublyLinkedListNode(SinglyLinkedListNode):
    def __init__(self, data=None, next_node=None, previous_node=None):
        SinglyLinkedListNode.__init__(self, data, next_node)
        self.previous_node = previous_node

class DoublyLinkedList(SinglyLinkedList):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_start(self, data):
        new_node = DoublyLinkedListNode(data, self.head, None)
        if self.head is not None:
            self.head.previous_node=new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def insert_end(self, data):
        new_node = DoublyLinkedListNode(data, None, self.tail)
        if self.tail is not None:
            self.tail.next_node = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
    
    def delete_end(self):
        temp = self.tail
        self.tail = self.tail.previous_node
        return temp

    @classmethod
    def create_from_list(cls, lst):
        lnklst =cls()
        for data in lst:
            lnklst.insert_end(data)
        return lnklst

    def delete_value(self, value):
        current = self.head
        previous = None
        while current is not None:
            if current.data == value:
                if previous is not None:
                    previous.next_node = current.next_node
                    current.next_node.previous_node = previous
                    return True
            previous = current
            current = current.next_node
    
    def delete_node(self, node):
        current = self.head
        previous = None
        while current is not None:
            if current == node:
                if previous is not None:
                    previous.next_node = current.next_node
                    current.next_node.previous_node = previous
                    return True
            previous = current
            current = current.next_node


    def reverse(self):
        self.tail = self.head
        current = self.head
        previous = None
        while current is not None:
            next = current.next_node
            current.next_node = previous
            if previous is not None:
                previous.previous_node = current
            previous = current
            current = next
        self.head = previous
    


if __name__ == '__main__':
    #lst = DoublyLinkedList()
    temp = DoublyLinkedList.create_from_list([1,2,3,4,4,5,6,6,7])
    print(temp)
    print(temp.find_midpoint().data)
    temp.delete_dupes()
    print(temp)