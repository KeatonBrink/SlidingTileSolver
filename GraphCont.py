from MyQueue import MyQueue
from HashTable import HashTable


class GraphData:
    def __init__(self):
        self.counter = 0
        self.path = []
        self.min = [None]


class Graph:
    def __init__(self, numVerticies):
        self.Graph = [[] for x in range(numVerticies)]
        self.GHashTable = HashTable(numVerticies)

    def AddGraphIndex(self, permutations):
        j = 0
        for i in permutations:
            curNode = [int(i), j]
            self.GHashTable.Insert(curNode)
            j += 1

    def StringStateToGraph(self, item):
        return self.GHashTable.Retrieve(item)

    def AddEdge(self, v0, v1):
        self.Graph[v0].append(v1)

    def AddEdgeParent(self, item):
        i = 1
        i1 = self.StringStateToGraph(int(item[0]))
        self.Graph[i1].append(item)
        while i < len(item):
            i2 = self.StringStateToGraph(int(item[i]))
            self.AddEdge(i1, i2)
            i += 1

    def isEdge(self, v0, v1):
        for elt in self.Graph[v0]:
            if elt == v1:
                return True
        return False

    def getNeighbors(self, v0):
        if len(self.Graph[v0]) == 0:
            return None
        return self.Graph[v0]

    def ReadableGameStateList(self, PathList):
        newPathList = []
        for i in PathList:
            newPathList.append(self.Graph[i][0][0])
        return newPathList

    def FindPath(self, v0, v1):
        q = MyQueue()
        From = [-1] * len(self.Graph)
        q.EnQ(v0)
        From[v0] = v0
        while q.Size() > 0:
            c = q.DeQ()
            if c == v1:
                currentInd = v1
                Path = [v1]
                while currentInd != v0:
                    Path.append(From[currentInd])
                    currentInd = From[currentInd]
                Path.reverse()
                return Path
            index = 0
            for elt in self.Graph[c]:
                if not index:
                    index = 1
                elif From[elt] == -1:
                    q.EnQ(elt)
                    From[elt] = c
        return None
