from abc import ABC, abstractmethod

class Heap(ABC):
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap_size = 0
        self.heap = [None]*capacity

    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i+1
    
    def right_child(self, i):
        return 2*i+2

    @abstractmethod
    def heapify(self):
        pass

    @abstractmethod
    def delete_key(self, int):
        pass
    
    @abstractmethod
    def insert_key(self, int):
        pass

    def __str__(self):
        return str(self.heap)


class MinHeap(Heap):
    def __init__(self, capacity):
        super().__init__(capacity)

    def insert_key(self, key):
        if self.capacity < self.heap_size:
            raise Exception('capacity full. Unable to add key')

        self.heap_size += 1
        index = self.heap_size -1
        self.heap[index] =  key

        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] =  self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def get_min(self):
        return self.heap[0]

    def extract_min(self):
        if self.heap_size <=0:
            return None
        
        if self.heap_size == 1:
            self.heap_size-=1
            return self.heap[0]

        root = self.heap[0]
        self.heap[0] = self.heap[self.heap_size-1]
        self.heap[self.heap_size-1]= None
        self.heap_size-=1
        self.heapify(0)

        return root

    def decrease_key(self, index, value):
        if index < 0:
            return None

        self.heap[index] = value

        while index !=0  and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] =  self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)


    def delete_key(self, index):
        self.decrease_key(index, float('-inf'))
        self.extract_min()


    def heapify(self, index):
        if self.heap[index] == None:
            return None
        left = self.left_child(index)
        right = self.right_child(index)
        smallest = index
        
        if(left < self.heap_size and self.heap[left] < self.heap[index]):
            smallest=left
        if(right < self.heap_size and self.heap[right] < self.heap[smallest]):
            smallest=right
        if(smallest != index):
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify(smallest)

def sort(heap):
    while heap.heap_size != 0:
        print(heap.extract_min())


if __name__ == '__main__':
    heappy = MinHeap(10)
    heappy.insert_key(10)
    heappy.insert_key(11)
    heappy.insert_key(9)
    heappy.insert_key(19)
    heappy.insert_key(6)
    heappy.insert_key(31)
    heappy.insert_key(14)
    heappy.insert_key(30)
    heappy.insert_key(22)
    heappy.insert_key(41)
    print(str(heappy))
    heappy.delete_key(8)
    print(str(heappy))
    heappy.decrease_key(6, 1)
    print(str(heappy))
