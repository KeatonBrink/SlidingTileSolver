def myPermutations(inputParams):
    curIndex = len(inputParams) - 1
    permCount = 1
    # List to return permutations starting with the initial permutation
    allPermutations = [''.join(map(str, inputParams))]
    prevPerm = inputParams[:]
    # While there are more permutations
    while curIndex >= 0:
        # Array to store temporarily popped parameters
        storeParams = []
        # Boolean for finding Perm
        foundPerm = False
        # Key is the value at the current index
        key = inputParams[curIndex]
        # Start popping including the target index
        j = curIndex
        # While more to pop
        while len(prevPerm)-1 - j >= 0:
            # Pop them
            storeParams.append(inputParams.pop())
            j += 1
        # For loop to find popped value that is bigger than the key
        for i in range(len(storeParams)):
            if not foundPerm and storeParams[i] > key:
                foundPerm = True
                minVal = i
            elif foundPerm and storeParams[i] < storeParams[minVal] and storeParams[i] != key:
                minVal = i
        # If popped value/new Permutation is not found move the curIndex back one
        if not foundPerm:
            inputParams = prevPerm[:]
            storeParams = []
            curIndex -= 1
            continue
        # else we continue by adding the new value to the key spot
        inputParams.append(storeParams.pop(minVal))
        # While loop to create the new smallest permutation
        while len(storeParams) > 0:
            i = 1
            storeIndex = 0
            minVal = storeParams[0]
            # Essentially find the smallest value in storeParams and add it to the new Permutation
            while i < len(storeParams):
                if minVal > storeParams[i]:
                    storeIndex = i
                    minVal = storeParams[i]
                i += 1
            inputParams.append(storeParams.pop(storeIndex))
        # Add the new permutation and move to the lowest possible location for new permutation
        allPermutations.append(''.join(map(str, inputParams)))
        permCount += 1
        prevPerm = inputParams[:]
        curIndex = len(prevPerm) - 2
    return allPermutations
