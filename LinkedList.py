class Node:
    def __init__(self, item, nextr=None):
        self.mItem = item
        self.mNext = nextr

# Still needs Exists and Size


class UUC:
    def __init__(self):
        self.mFirst = None
        self.mLast = self.mFirst

    def Delete(self, item):
        if not self.Exists(item):
            return False
        if self.mFirst.mItem == item:
            self.mFirst = self.mFirst.mNext
            return True
        current = self.mFirst
        while not current.mNext.mItem == item:
            current = current.mNext
        current.mNext = current.mNext.mNext
        return True

    def Size(self):
        count = 0
        current = self.mFirst
        while not (current == None):
            count += 1
            current = current.mNext
        return count

    def Retrieve(self, item):
        if not self.Exists(item):
            return None
        current = self.mFirst
        while not (current.mItem == item):
            current = current.mNext
        return current.mItem

    def Insert(self, item):
        if self.mFirst is None:
            self.mFirst = Node(item, self.mFirst)
            self.mLast = self.mFirst
        else:
            self.mLast.mNext = Node(item)
            self.mLast = self.mLast.mNext

    def Traverse(self, callbackr):
        current = self.mFirst
        while current != None:
            callbackr(current.mItem)
            current = current.mNext

    def Exists(self, item):
        current = self.mFirst
        while current:
            if current.mItem == item:
                return True
            current = current.mNext
        return False
