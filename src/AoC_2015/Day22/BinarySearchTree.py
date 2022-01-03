from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):

    def __init__(self, value: T):
        self.parent: Node[T] = None
        self.left: Node[T] = None
        self.right: Node[T] = None
        self.value: T = value

    def add_child(self, value: T):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
                self.left.parent = self
            else:
                self.left.add_child(value)
        else:
            if self.right is None:
                self.right = Node(value)
                self.right.parent = self
            else:
                self.right.add_child(value)


class BinarySearchTree(Generic[T]):

    def __init__(self):
        self.root: Node[T] = None

    def insert(self, value: T):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.add_child(value)

    def pop_left(self) -> T:
        node = self.root
        while node.left is not None:
            node = node.left

        if node.right is not None:
            node.right.parent = node.parent
            if node == self.root:
                self.root = node.right
            else:
                node.parent.left = node.right

        return node.value
