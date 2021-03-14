class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    def put(self, key, val):
        self.root = self.__insert(self.root, key, val)
    
    def __insert(self, n, key, val):
        if n is None:
            return Node(key, val)
        if key>n.key:
            n.right = self.__insert(n.right, key, val)
        if key < n.key:
            n.left = self.__insert(n.left, key, val)
        if key == n.key:
            n.val = val
        return n
    
    def inorder(self):
        self.__inorder(self.root)
    
    def __inorder(self, n):
        if n is None:
            return
        self.__inorder(n.left)
        print("key = {} val = {}".format(n.key,n.val))
        self.__inorder(n.right)

if __name__ == '__main__':
    b = BST()
    b.put(5, "five")
    b.put(3, "3")
    b.put(2, "two")
    b.put(8, "8")
    b.put(6, "six")
    b.put(9, "nine")
    b.inorder()