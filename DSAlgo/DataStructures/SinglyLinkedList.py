class SinglyLinkedListNode:
    def __init__(self, data=None, next=None):
       self.data = data
       self.next = next
    
    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_start(self, data):
        new_node = SinglyLinkedListNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data):
        new_node = SinglyLinkedListNode(data)
        if self.head == None:
            self.head = new_node
            return
        node = self.head
        while node.next !=None:
            node = node.next
        node.next=new_node

    def delete_start(self):
        if self.head is None:
            return
        temp = self.head
        self.head= self.head.next
        return temp
    
    def delete_end(self):
        if self.head == None:
            return
        node = self.head
        previous = None
        while node.next is not None:
            previous = node
            node = node.next
        if previous is not None:
            previous.next = node.next
        else:
            self.head = node.next
        return node
        
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        node = self.head
        previous = None
        while node is not None:
            if node.data == data:
                break
            previous = node
            node = node.next
        if node is None:
            return
        previous.next = node.next
            
        
    def __str__(self):
        node = self.head
        st = ''
        while node !=None:
            st += str(node.data) + ' '
            node = node.next
        return st

    @classmethod
    def create_from_list(cls, lst):
        lnklst = cls()
        for data in lst:
            lnklst.insert(data)
        return lnklst

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        raise StopIteration
    
    def find(self, value):
        node = self.head
        while node is not None:
            if node.data == value:
                return True
            node = node.next_node
        return False

    def __len__(self):
        i=0
        node = self.head
        while node is not None:
            i+=1
            node = node.next
        return i
        
    def reverse(self):
        current = self.head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
    
    def find_midpoint(self):
        slow = fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def nth_node_from_end(self, n):
        i = 0 
        node = self.head
        while node is not None and i <= n:
            i+=1
            node = node.next
            if node is None:
                return
        behind = self.head
        while node is not None:
            node = node.next
            behind = behind.next
        return behind
    
    def delete_dupes(self):
        dictionary = {}
        node = self.head
        previous = None
        while node is not None:
            if node.data in dictionary.keys():
                previous.next = node.next
            else:
                dictionary[node.data] = None
            previous = node
            node = node.next
           

def sort_list_inplace_with3elements(lst):
    lst0, lst1, lst2 = [SinglyLinkedList() for _ in range(3)]
    lst0.insert_start(SinglyLinkedListNode())
    print(lst0)
    print(lst1)
    print(lst2)

if __name__ == '__main__':
    lst = SinglyLinkedList.create_from_list([1,2,3,4,5,6])
    print(lst.find_midpoint())
    print(len(lst))
    for item in lst:
        print(item.data)
