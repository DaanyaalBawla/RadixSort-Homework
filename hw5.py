class Queue:
    def __init__(self):
        self.items = []

        self.frontIdx = 0

    def __compress(self):
        newlst = []
        for i in range(self.frontIdx, len(self.items)):
            newlst.append(self.items[i])
        self.items = newlst
        self.frontIdx = 0

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty queue")
    # When queue is half full, compress it. Does not let the list
    # continue to grow unchecked.
        if self.frontIdx * 2 > len(self.items):
            self.__compress()

        item = self.items[self.frontIdx]
        self.frontIdx += 1
        return item

    def traverse(self):
        print(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to access front of empty queue")

        return self.items[self.frontIdx]

    def isEmpty(self):
        return self.frontIdx == len(self.items)

    def radsort(self):
        queuelist = {" ": Queue(), "a": Queue(), "b": Queue(), "c": Queue(), "d": Queue(), "e": Queue()}
        node = []
        while self.isEmpty() is not True:
            remove = self.dequeue()
            node.append(remove)
        self.items.clear()
        self.frontIdx = 0
        for s in node:
            if len(s) > 1:
                queuelist[s[1]].enqueue(s)
            else:
                queuelist[" "].enqueue(s)
        node.clear()
        for s in sorted(queuelist.keys()):
            while not queuelist[s].isEmpty():
                ds = queuelist[s].dequeue()
                self.enqueue(ds)
        for v in queuelist.values():
            while not v.isEmpty():
                v.dequeue()
        node.clear()
        self.frontIdx = 0
        while self.isEmpty() is not True:
            remove = self.dequeue()
            node.append(remove)
        self.items.clear()
        self.frontIdx = 0
        for n in node:
            if len(n) > 0:
                queuelist[n[0]].enqueue(n)
            else:
                queuelist[" "].enqueue(n)
        node.clear()
        self.frontIdx = 0
        for k in sorted(queuelist.keys()):
            while not queuelist[k].isEmpty():
                ds = queuelist[k].dequeue()
                self.enqueue(ds)
        return


q = Queue()
test = ["dc", "ba", "e", "c", "b"]
for c in test:
    q.enqueue(c)
q.radsort()
q.traverse()
