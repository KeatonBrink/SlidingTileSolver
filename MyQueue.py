class MyQueue:
    def __init__(self):
        self.mQueue = []

    def EnQ(self, item):
        self.mQueue.append(item)

    def DeQ(self):
        return self.mQueue.pop(0)

    def Size(self):
        return len(self.mQueue)
