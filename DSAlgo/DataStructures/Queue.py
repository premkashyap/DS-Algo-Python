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
    
    def __len__(self):
        return len(self.queue)

    def __iter__(self):
        for item in self.queue[::-1]:
            yield item
        raise StopIteration
    

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    for item in queue:
        print(item)
