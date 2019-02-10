class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def is_present(self, data):
        return data in self.stack

    def create_from_list(self, lst):
        self.stack = lst[::-1]
    
    def __str__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)

    def __iter__(self):
        for item in self.stack[::-1]:
            yield item
        raise StopIteration

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    for item in stack:
        print(item)