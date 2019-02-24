

class DLLNode():

    def __init__(self, value, prev, nxt):
        self.value = value
        self.prev = prev
        self.next = nxt

    def __repr__(self):
        nval = self.next.value if self.next else None
        pval = self.prev.value if self.prev else None
        return "[{}:{}:{}]".format(repr(pval),
                                   self.value,
                                   repr(nval))

class DoubleLinkedList():

    def __init__(self):
        self.begin = None
        self.end = None
        self._count = 0

    def _invariant(self):
        if self._count == 0:
            assert self.begin == None
            assert self.end == None
        elif self._count == 1:
            assert self.begin == self.end
        else:
            assert self.begin.prev == None
            assert self.begin.next != None
            assert self.end.next == None
            assert self.end.prev != None

    def push(self, obj):
        self._invariant()
        if not self.begin:
            self.begin = DLLNode(obj, None, None)
            self.end = self.begin
        else:
            last = self.end
            self.end = DLLNode(obj, last, None)
            last.next = self.end
        self._count += 1

    def pop(self):
        self._invariant()
        if self._count == 0:
            return None
        elif self._count == 1:
            value = self.begin.value
            self.begin = None
            self.end = None
            self._count = 0
            return value
        else:
            value = self.end.value
            self.end = self.end.prev
            self.end.next = None
            self._count -= 1
            return value

    def shift(self, obj):
        self._invariant()
        if self._count == 0:
            self.begin = DLLNode(obj, None, None)
            self.end = self.begin
        else:
            first = self.begin
            self.begin = DLLNode(obj, None, self.begin)
            first.prev = self.begin
        self._count += 1


    def unshift(self):
        self._invariant()
        if self._count == 0:
            return None
        elif self._count == 1:
            value = self.begin.value
            self.begin = None
            self.end = None
            self._count = 0
            return value
        else:
            value = self.begin.value
            self.begin = self.begin.next
            self.begin.prev = None
            self._count -= 1
            return value

    def detach_node(self, node):
        prev = node.prev
        nxt = node.next
        if prev:
            prev.next = nxt
        else:
            self.begin = nxt
        if nxt:
            nxt.prev = prev
        else:
            self.end = prev
        self._count -= 1

    def remove(self, obj):
        self._invariant()
        if self._count == 0:
            return
        elif self._count == 1:
            if self.begin.value == obj:
                self.begin = None
                self.end = None
                self._count = 0
                return 0
        else:
            node = self.begin
            location = 0
            while node != None:
                if node.value == obj:
                    self.detach_node(node)
                    return location
                node = node.next
                location += 1

    def first(self):
        self._invariant()
        return self.begin.value

    def last(self):
        self._invariant()
        return self.end.value

    def count(self):
        self._invariant()
        return self._count

    def get(self, index):
        self._invariant()
        if self.begin == None:
            return
        location = 0
        node = self.begin
        while node != self.end:
            if index == location:
                return node.value
            node = node.next
            location += 1
        if index == location:
            return self.end.value


    def dump(self, mark):
        self._invariant()
        node = self.begin
        while node != self.end:
            print(node.value)
            node = node.next
        print(node.value)

