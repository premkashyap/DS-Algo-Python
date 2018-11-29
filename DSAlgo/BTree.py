from Queue import Queue
from DoubleLinkedList import DoublyLinkedList, DoublyLinkedListNode

class BTreeNode:
    def __init__(self, data=None, left=None, right=None):
       self.data = data
       self.left = left
       self.right = right

    def __str__(self):
        print(str(self.data))

    def insert(self, data):
        if self.data > data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = BTreeNode(data)
        elif self.data < data:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = BTreeNode(data)
        else:
            return

    def find(self, data):
        if self.data > data:
            return self.right.find(data) if self.right is not None else False
        elif self.data < data:
            return self.left.find(data) if self.left is not None else False
        else:
            return True
    
    def inorder_traversal(self):
        if self.left is not None:
            self.left.inorder_traversal()
        print(self.data)
        if self.right is not None:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.data)
        if self.left is not None:
            self.left.preorder_traversal()
        if self.right is not None:
            self.right.preorder_traversal()
        
    def postorder_traversal(self):
        if self.left is not None:
            self.left.postorder_traversal()
        if self.right is not None:
            self.right.postorder_traversal()
        print(self.data)

    def levelorder_traversal(self):
        queue = Queue()
        print(self.data)
        if(self.left is not None):
            queue.enqueue(self.left)
        if(self.right is not None):
            queue.enqueue(self.right)
        while len(queue) !=0:
            queue.dequeue().data.levelorder_traversal()

    def calculate_height(self):
        return 1 + max(0 if self.left is None else self.left.calculate_height(), 0 if self.right is None else self.right.calculate_height())
    
    def print_leaf_nodes(self):
        if self.left is None and self.right is None:
            print(self.data)
        if self.left is not None:
            self.left.print_leaf_nodes()
        if self.right is not None:
            self.right.print_leaf_nodes()

    def find_number_of_leaf_nodes(self):
        if self.left is None and self.right is None:
            return 1
        else:
            return (self.left.find_number_of_leaf_nodes() if self.left is not None else 0 ) + (self.right.find_number_of_leaf_nodes() if self.right is not None else 0) 
        
    def is_tree_balanced(self):
        return (self.left.calculate_height() if self.left is not None else 0) == (self.right.calculate_height() if self.right is not None else 0)

    def delete(self, val):
        if self.data == val:
            self._deletion()
        elif self.data > val:
            self.left=self.left.delete(val)
        else:
            self.right=self.right.delete(val)
        return self

    def _deletion(self):
        if self.left is None and self.right is None:
            return None
        elif self.left is None and self.right is not None:
            return self.right
        elif self.right is None and self.left is not None:
            return self.left
        else:
            if self.right.left is None:
                self.data = self.right.data
                temp = self.right
                self.right= self.right.right
                temp = None
                return
            node = self.right.left
            parent = self.right
            while node.left is not None:
                parent = node
                node = node.left
            self.data=node.data
            parent.left = node.right
            return
            
                
   

if __name__ == '__main__':
    Tree = BTreeNode(10)
    Tree.insert(6)
    Tree.insert(8)
    Tree.insert(5)
    Tree.insert(13)
    Tree.insert(12)
    Tree.insert(14)
    Tree.insert(16)
    Tree.inorder_traversal()
    Tree.delete(10)
    print('value deleted. New Tree below')
    Tree.inorder_traversal()

    # Tree.inorder_traversal()
    # print('-------------------------')
    # Tree.postorder_traversal()
    # print('-------------------------')
    # Tree.preorder_traversal()
    # print('-------------------------')
    # Tree.levelorder_traversal()
    # print(Tree.find(100))
    # print(Tree.find(10))
    # Tree.print_leaf_nodes()
    # print(Tree.find_number_of_leaf_nodes())

    # Tree1 = BTreeNode(10)
    # Tree1.insert(20)
    # print(Tree1.is_tree_balanced())