
class BSTreeNode:

    def __init__(self, parent, left, right, key, value):
        self.parent = parent
        self.left = left
        self.right = right
        self.key = key
        self.value = value

    def __repr__(self):
        pkey = parent.key if parent else None
        lkey = left.key if left else None
        rkey = right.key if right else None
        return "{}:{{}:{}}:{}:{}".format(
            self.parent,
            self.key,
            self.value,
            self.left,
            self.right,
        )


class BSTree:

    def __init__(self):
        self.root = None
        self._count = 0

    def get(self, key):
        if self._count == 0:
            return
        elif self._count == 1:
            if key == self.root.key:
                return self.root.value
            else:
                return
        else:
            node = self.root

            while node:
                if node.key == key:
                    return node.value
                if key < node.key:
                    node = node.left
                else:
                    node = node.right

    def set(self, key, value):
        if self._count == 0:
            self.root = BSTreeNode(None, None, None, key, value)
            self._count = 1
        else:
            node = self.root

            while node:
                if key == node.key:
                    node.value = value
                    return
                elif key < node.key:
                    if node.left:
                        node = node.left
                    else:
                        node.left = BSTreeNode(node,
                                               None,
                                               None,
                                               key,
                                               value)
                        self._count += 1
                        return
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = BSTreeNode(node,
                                                None,
                                                None,
                                                key,
                                                value)
                        self._count += 1
                        return

    def _find_minimum(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, node):
        if self._count == 0:
            return
        if not node.left and not node.right:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            self._count -= 1
        elif not node.left and node.right:
            node = node.right
            self._count -= 1
        elif not node.right and node.left:
            node = node.left
            self._count -= 1
        else:
            min_node = self._find_minimum(node.right)
            node.key = min_node.key
            node.value = min_node.value
            self.delete(min_node)

    def remove(self, key):
        if self._count == 0:
            return
        node = self.root
        while node:
            if node.key == key:
                self.delete(node)
                return
            if key < node.key:
                node = node.left
            else:
                node = node.right





