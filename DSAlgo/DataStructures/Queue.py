class Queue():
    
    def __init__(self):
        self.queue = []
    
    def peek(self):
        return self.queue[-1]

    def is_present(self, data):
        return data in self.queue

    def create_from_list(self, lst):
        self.queue = lst
    
    def __str__(self):
        return str(self.queue)

    def enqueue(self, data):
        self.queue.insert(0, data)
    
    def dequeue(self):
        return self.queue.pop()
    

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    print(queue)
    print(queue.dequeue())
    print(queue)
