from SinglyLinkedList import BaseLinkedList

class Stack(BaseLinkedList):

    def insert_start(self, data):
        raise AttributeError

    def delete_start(self):
        raise AttributeError

    def push(self, data):
        BaseLinkedList.insert_end(self, data)
    
    def pop(self):
        return BaseLinkedList.delete_end(self)


if __name__ == '__main__':
    lst = Stack()
    temp = Stack.create_from_list([1,2])
    print(temp)
    temp.push(10)
    print(temp)
    print(temp.pop())
    temp.pop()
    temp.pop()
    print(temp)