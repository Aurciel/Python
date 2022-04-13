def arrayManipulation(n):
    maxColumnSize  = 3*int(n)
    maxRowSize = 3*int(n)
    i = 0
    j = 0
    mainArray = []
    rowArray = []

    while j < maxRowSize :
        while i < maxColumnSize:
            rowArray.append((i+j)%3)
            i+=1
        
        mainArray.append(rowArray)
        j+=1
        i=0
        rowArray = [] 
    
    return mainArray

resultingArray = arrayManipulation(input("Enter N for a 3 x N matrix: "))
print(resultingArray)