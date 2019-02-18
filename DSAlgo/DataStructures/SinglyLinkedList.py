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
        while node.next is not None:
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

    def delete_at_position(self, position):
        if position == 0:
            self.head = self.head.next
        else:
            i = 0
            node = self.head
            while i < position-1:
                i+=1
                node = node.next
            node.next = node.next.next if node.next is not None else None
            
        
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

def getNodeFromTail(head, positionFromTail):
    current = result = head
    pos = 0
    while current is not None:
        if pos > positionFromTail:
            result = result.next
        pos+=1
        current = current.next
    return result.data    

def reversePrint(head):
    stack = []
    node = head
    while node is not None:
        stack.append(node.data)
        node = node.next
    while len(stack) != 0:
        print(stack.pop())

def delete_dupes(head):
    data_lookup = {}
    node = head
    previous = None
    while node is not None:
        if node.data not in data_lookup.keys():
            data_lookup[node.data] = None
            previous = node
        else:
            previous.next = node.next
        node = node.next      
    return head      

def sort_list_inplace_with3elements(lst):
    lst0, lst1, lst2 = [SinglyLinkedList() for _ in range(3)]
    lst0.insert_start(SinglyLinkedListNode())
    print(lst0)
    print(lst1)
    print(lst2)


def has_cycle(head):
    if head is None or head.next is None:
        return True
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

def deleteNode(head, position):
    if position == 0:
        return head.next
    head.next = deleteNode(head.next , position-1)
    return head

def compare_lists(llist1, llist2):
    if llist1 is None and llist2 is None:
        return True
    elif (llist1 is None) or (llist2 is None):
        return False
    else:
        return (llist1.data == llist2.data) and compare_lists(llist1.next, llist2.next)

def mergeLists(head1, head2):
    if head1 is None and head2 is None:
        return
    elif head1 is None:
        return head2
    elif head2 is None:
        return head1
    elif head1.data < head2.data:
        head1.next = mergeLists(head1.next, head2)
        return head1
    else:
        head2.next = mergeLists(head1, head2.next)
        return head2

if __name__ == '__main__':
    lst = SinglyLinkedList.create_from_list([1,2,3,4,5,6])
    print(lst.find_midpoint())
    print(len(lst))
    for item in lst:
        print(item.data)
