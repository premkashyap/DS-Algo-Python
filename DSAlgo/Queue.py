from SinglyLinkedList import BaseLinkedList

class Queue(BaseLinkedList):

    def insert_start(self, data):
        raise AttributeError

    def delete_end(self):
        raise AttributeError

    def enqueue(self, data):
        BaseLinkedList.insert_end(self, data)
    
    def dequeue(self):
        return BaseLinkedList.delete_start(self)
    

if __name__ == '__main__':
    lst = Queue()
    temp = Queue.create_from_list([1,2,3,4,4,5,6,6,7])
    print(temp)
    temp.enqueue(10)
    print(temp)
    temp.dequeue()
    temp.dequeue()
    temp.dequeue()
    print(temp)