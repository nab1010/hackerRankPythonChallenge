N,M = input().split( )
N = int(N) #row
M = N*3 #col
midRow = int(N /2)+1
midCol = int(M/2)+1
for row in  range(N):
    rowText = ""
    timesInsert = 2*((midRow - abs(midRow - row -1)))-1
    numCharacters = timesInsert*3
    if row == midRow - 1:
        for col in range ((midCol - 1) - int(7/2)):
            rowText += "-"
        rowText += "WELCOME"
        for col in range ((midCol - 1) + int(7/2) + 1, M):
            rowText += "-"
    else:
        for col in range((midCol - 1) - int(numCharacters/2)):           
            rowText += "-"
        for numInsert in range (timesInsert):
            rowText += ".|."
        for col in range ((midCol - 1) + int(numCharacters/2) + 1, M):
            rowText += "-"
    print(rowText)
