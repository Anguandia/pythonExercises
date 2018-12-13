'''a function to print the first five squares of natural numbers'''
def printList():
    result = []
    for num in range(1, 21):
        sq = num**2
        result.append(sq)
    print(result[0:5])


printList() # test function
