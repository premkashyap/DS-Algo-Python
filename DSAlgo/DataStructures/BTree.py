from Queue import Queue
from DoublyLinkedList import DoublyLinkedList, DoublyLinkedListNode

class BTreeNode:
    def __init__(self, data=None, left=None, right=None):
       self.data = data
       self.left = left
       self.right = right

    def __str__(self):
        return str(self.data)

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
        print(self.data, end = ' ')
        if self.right is not None:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.data, end = ' ')
        if self.left is not None:
            self.left.preorder_traversal()
        if self.right is not None:
            self.right.preorder_traversal()
        
    def postorder_traversal(self):
        if self.left is not None:
            self.left.postorder_traversal()
        if self.right is not None:
            self.right.postorder_traversal()
        print(self.data, end=' ')


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

    def sum_of_all_nodes(self):
        return self.data + (self.left.sum_of_all_nodes() if self.left is not None else 0 ) + (self.right.sum_of_all_nodes() if self.right is not None else 0)

def LowestCommonAncestor(root, v1, v2):
        if root.info > v1 and root.info > v2:
            return LowestCommonAncestor(root.left, v1, v2)
        elif root.info < v1 and root.info < v2:
            return LowestCommonAncestor(root.right, v1, v2)
        else:
            return root

def height(root):
    return 0 if root.left is None and root.right is None else 1 + max(0 if root.left is None else height(root.left), 0 if root.right is None else height(root.right))

def is_tree_balanced(root):
    return (height(root.left) if root.left is not None else 0) == (height(root.right) if root.right is not None else 0)   

def print_leaf_nodes(root):
    if root.left is None and root.right is None:
        print(root.data, end=' ')
    elif root.left is not None:
        print_leaf_nodes(root.left)
    elif root.right is not None:
        print_leaf_nodes(root.right)

def number_of_leaf_nodes(root):
    if root.left is None and root.right is None:
        return 1
    else:
        return (number_of_leaf_nodes(root.left) if root.left is not None else 0 ) + (number_of_leaf_nodes(root.right) if root.right is not None else 0) 
        
def _vertical_view(BTreeNode, i, lookup):
    if BTreeNode is None:
        return
    if i in lookup.keys():
        lookup[i].append(BTreeNode)
    else:
        lookup[i] = []
        lookup[i].append(BTreeNode)
    _vertical_view(BTreeNode.left, i-1, lookup)
    _vertical_view(BTreeNode.right, i+1, lookup)
    return lookup

def vertical_view(BTreeNode):
    lookup = _vertical_view(BTreeNode, 0, {})
    for key in sorted(lookup.keys()):
        for node in lookup[key]:
            print(node, end=' ')
        print()

def top_view(BTreeNode):
    if BTreeNode == None:
        return 
    queue = []
    top_view = {}
    i=0
    queue.append((BTreeNode, i))
    while len(queue) != 0:
        node = queue.pop(0)
        level = node[1]
        if level not in top_view.keys():
            top_view[level] = node[0]
        if node[0].left is not None:
            queue.append((node[0].left, level-1))
        if node[0].right is not None:
            queue.append((node[0].right, level+1))
    for key in sorted(top_view.keys()):
        print(top_view[key])
        
def bottom_view(BTreeNode):
    if BTreeNode == None:
        return 
    queue = []
    top_view = {}
    i=0
    queue.append((BTreeNode, i))
    while len(queue) != 0:
        node = queue.pop(0)
        level = node[1]
        if level not in top_view.keys():
            top_view[level] = []
            top_view[level].append(node[0])
        else:
            top_view[level].append(node[0])
        if node[0].left is not None:
            queue.append((node[0].left, level-1))
        if node[0].right is not None:
            queue.append((node[0].right, level+1))
    for key in sorted(top_view.keys()):
        print(top_view[key][-1])

def side_view(BTreeNode):
    if BTreeNode == None:
        return 
    queue = []
    side_view = {}
    queue.append((BTreeNode, 0))
    while len(queue) != 0:
        node = queue.pop(0)
        level = node[1]
        if level not in side_view.keys():
            side_view[level] = node[0]
        if node[0].left is not None:
            queue.append((node[0].left, level+1))
        if node[0].right is not None:
            queue.append((node[0].right, level+1))
    for key in sorted(side_view.keys()):
        print(side_view[key])

def mirror_image_tree(root):
    if root == None:
        return 
    root.left, root.right = root.right, root.left
    mirror_image_tree(root.left)
    mirror_image_tree(root.right)

def levelorder_traversal(root):
    queue = []
    node = root
    while node:
        print(node.data, end = ' ')
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        node = queue.pop(0)

def zig_zag_level_order(node):
    if node is None:
        return
    print(node.data, end = ' ')
    queue = []
    stack = []
    queue.insert(0, node.left)
    queue.insert(0, node.right)
    while len(queue) != 0 or len(stack) != 0:
        while len(queue) != 0:
            node = queue.pop()
            print(node.data, end = ' ')
            stack.append(node.left)
            stack.append(node.right)
        while len(stack)!=0:
            queue.insert(0, stack.pop())
        



if __name__ == '__main__':
    Tree = BTreeNode(100)
    Tree.insert(50)
    Tree.insert(150)
    Tree.insert(25)
    Tree.insert(75)
    Tree.insert(125)
    Tree.insert(175)
    Tree.insert(12)
    Tree.insert(37)
    Tree.insert(67)
    Tree.insert(90)
    Tree.insert(112)
    Tree.insert(137)
    Tree.insert(165)
    Tree.insert(200)
    levelorder_traversal(Tree)
    print('\n')
    zig_zag_level_order(Tree)

    # vertical_view(Tree)
    # print()
    # top_view(Tree)
    # print()
    # bottom_view(Tree)
    # print()
    # side_view(Tree)
    
    # Tree.inorder_traversal()
    # mirror_view(Tree)
    # print('\n' + '*'*10)
    # Tree.inorder_traversal()

