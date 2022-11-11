from myPermutation import myPermutations
from LinkedList import UUC
from GraphCont import Graph


def main():
    masterArray = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    LL = UUC()
    comb = myPermutations(masterArray)
    for i in comb:
        # Calculate potential neighbors
        curNode = i
        curNode = findNeighbors(curNode)
        LL.Insert(curNode)
    myGraph = Graph(LL.Size())
    myGraph.AddGraphIndex(comb)
    LL.Traverse(myGraph.AddEdgeParent)
    userStart = input("Enter a random permutation of 9 digits: ")
    Path = myGraph.FindPath(myGraph.StringStateToGraph(
        userStart), myGraph.StringStateToGraph(comb[0]))
    Path = myGraph.ReadableGameStateList(Path)
    printPath(Path)
    tree = 1


def printPath(Path):
    if Path is None:
        print(None)
        return
    for i in Path:
        curString = list(i)
        print(curString[0] + " | " + curString[1] + " | " + curString[2])
        print("---------")
        print(curString[3] + " | " + curString[4] + " | " + curString[5])
        print("---------")
        print(curString[6] + " | " + curString[7] + " | " + curString[8])
        print("\n\n")


def findNeighbors(curState):
    returnList = [curState]
    testNode = list(curState)
    i1 = testNode.index('0')
    if i1 % 3 != 2:
        testNode[i1], testNode[i1+1] = testNode[i1+1], testNode[i1]
        testNode = "".join(testNode)
        returnList.append(testNode)
        testNode = list(curState)
    if i1 < 6:
        testNode[i1], testNode[i1+3] = testNode[i1+3], testNode[i1]
        testNode = "".join(testNode)
        returnList.append(testNode)
        testNode = list(curState)
    if i1 % 3 != 0:
        testNode[i1], testNode[i1-1] = testNode[i1-1], testNode[i1]
        testNode = "".join(testNode)
        returnList.append(testNode)
        testNode = list(curState)
    if i1 > 2:
        testNode[i1], testNode[i1-3] = testNode[i1-3], testNode[i1]
        testNode = "".join(testNode)
        returnList.append(testNode)
        testNode = list(curState)
    return returnList


main()
