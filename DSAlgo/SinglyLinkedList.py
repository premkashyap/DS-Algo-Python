class SinglyLinkedListNode:
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next_node = next_node
    
    def __str__(self):
        return str(self.data)


class BaseLinkedList:
    def __init__(self, head=None):
            self.head = head

    def insert_start(self, data):
        new_node = SinglyLinkedListNode(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = SinglyLinkedListNode(data)
        if self.head == None:
            self.head = new_node
            return
        node = self.head
        while node.next_node !=None:
            node = node.next_node
        node.next_node=new_node

    def delete_start(self):
        temp = self.head
        self.head= self.head.next_node
        return temp
    
    def delete_end(self):
        if self.head ==None:
            return
        node = self.head
        if self.head.next_node== None:
            self.head = None
            return
        while node.next_node.next_node is not None:
            node = node.next_node
        temp = node.next_node
        node.next_node= None
        return temp
        
    def __str__(self):
        node = self.head
        st = ''
        while node !=None:
            st += str(node.data) + ' '
            node = node.next_node
        return st

    @classmethod
    def create_from_list(cls, lst):
        lnklst =cls()
        for data in lst:
            lnklst.insert_end(data)
        return lnklst

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next_node
        raise StopIteration
    
    def find(self, value):
        node = self.head
        while node is not None:
            if node.data == value:
                return True
            node = node.next_node
        return False

    def __len__(self):
        i =0
        node = self.head
        while node is not None:
            i+=1
            node = node.next_node
        return i
        
class SinglyLinkedList(BaseLinkedList):

    def delete_value(self, value):
        current = self.head
        previous = None
        while current is not None:
            if current.data == value:
                if previous is not None:
                    previous.next_node = current.next_node
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
                    return True
            previous = current
            current = current.next_node


    def reverse(self):
        current = self.head
        previous = None
        while current is not None:
            next = current.next_node
            current.next_node = previous
            previous = current
            current = next
        self.head = previous
    
    def find_midpoint(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next_node is not None:
            slow = slow.next_node
            fast = fast.next_node.next_node
        return slow

    def nth_node_from_end(self, n):
        i =0 
        node = self.head
        while node is not None and i <= n:
            i+=1
            node = node.next_node
            if node is None:
                return None
        behind = self.head
        while node is not None:
            node = node.next_node
            behind = behind.next_node
        return behind
    
    def delete_dupes(self):
        dictionary = {}
        node = self.head
        while node is not None:
            if node.data in dictionary.keys():
                self.delete_node(node)
            else:
                dictionary[node.data] = None
            node = node.next_node


                


if __name__ == '__main__':
    lst = SinglyLinkedList()
    temp = SinglyLinkedList.create_from_list([1,2,3,4,4,5,6,6,7])
    print(temp)
    print(temp.find_midpoint().data)
    temp.delete_dupes()
    print(temp)