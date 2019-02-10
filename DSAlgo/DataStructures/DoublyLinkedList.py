class DoublyLinkedListNode():
    def __init__(self, data=None, next_node=None, previous_node=None):
        self.data = data
        self.next = next_node
        self.previous = previous_node
    def __str__(self):
        return str(self.data)

class DoublyLinkedList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __str__(self):
        node = self.head
        string = ''
        while node is not None:
            string+=str(node)
            string+=' '
            node = node.next
        return string

    def __len__(self):
        len = 0
        node = self.head
        while node is not None:
            len+=1
            node = node.next
        return len

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        raise StopIteration

    def insert_head(self, data):
        new_node = DoublyLinkedListNode(data, self.head, None)
        if self.head is not None:
            self.head.previous=new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def insert(self, data):
        new_node = DoublyLinkedListNode(data, None, self.tail)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
    
    def delete_tail(self):
        temp = self.tail
        self.tail = self.tail.previous
        self.tail.next = None
        if self.tail is None:
            self.head = None
        return temp

    def delete_head(self):
        temp = self.head
        self.head = self.head.next
        self.head.previous = None
        if self.head is None:
            self.tail = None
        return temp


    @classmethod
    def create_from_list(cls, lst):
        lnklst =cls()
        for data in lst:
            lnklst.insert(data)
        return lnklst

    def delete(self, value):
        if self.head is None:
            return
        current = self.head
        if self.head.data == value:
            self.head = self.head.next
            self.head.previous = None
            return current
        if self.tail.data == value:
            temp = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            return temp
        while current is not None:
            if current.data == value:
                if current.previous is not None:
                    current.previous.next = current.next
                if current.next is not None:
                    current.next.previous = current.previous
            current = current.next


    def reverse(self):
        current = self.head
        self.tail, self.head = self.head, self.tail
        while current is not None:
            next = current.next
            current.next = current.previous
            current.previous = next
            current = next
    

if __name__ == '__main__':
    lst = DoublyLinkedList.create_from_list([1,2,3])
    print(lst)
    lst.reverse()
    print(lst)
