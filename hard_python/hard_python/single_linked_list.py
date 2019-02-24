

class SLLNode():

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next.value if self.next else None
        return "[{}:{}]".format(self.value, repr(nval))

class SingleLinkedList():

    def __init__(self):
        self.begin = None
        self.end = None
        self._count = 0

    def push(self, obj):
        if not self.begin:
            self.begin = SLLNode(obj, None)
            self.end = self.begin
            self._count = 1
        else:
            self._count += 1
            last = self.end
            self.end = SLLNode(obj, None)
            last.next = self.end

    def pop(self):
        if self.begin == None:
            return None
        elif self.begin.next == None:
            value = self.begin.value
            self.begin = None
            self._count = 0
            return value

        node = self.begin
        while node.next != self.end:
            node = node.next

        value = self.end.value
        node.next = None
        self.end = node
        self._count -= 1
        return value

    def shift(self, obj):
        if self.begin == None:
            self.begin = SLLNode(obj, self.begin)
            self.end = self.begin
        else:
            self.begin = SLLNode(obj, self.begin)

        self._count += 1

    def unshift(self):
        if self.begin == None:
            return None

        value = self.begin.value
        self.begin = self.begin.next
        return value

    def remove(self, obj):
        if self.begin == None:
            return
        node = self.begin
        location = 0
        previous = None
        while node != self.end:
            if node.value == obj:
                if previous:
                    previous.next = node.next
                else:
                    self.begin = node.next
                self._count -= 1
                return location
            previous = node
            node = node.next
            location += 1

        if node.value == obj:
            if previous:
                previous.next = None
                self.end = previous
            else:
                self.begin = self.end 
            self._count -= 1
            return location

    def first(self):
        return self.begin.value

    def last(self):
        return self.end.value

        if self.begin == None:
            return
        node = self.begin
        while node.next != self.end:
            node = node.next
        return node.value

    def count(self):
        return self._count
        if self.begin == None:
            return 0
        count = 1
        node = self.begin
        while node.next != self.end:
            count += 1
            node = node.next
        return count

    def get(self, index):
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
        node = self.begin
        while node != self.end:
            print(node.value)
            node = node.next
        print(node.value)

