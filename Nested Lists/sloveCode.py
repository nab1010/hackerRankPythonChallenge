def findLowScore(pythonStudents):
    lowScoreIndex = 0
    for i in range (1, len(pythonStudents)):
        if pythonStudents[lowScoreIndex][1] > pythonStudents[i][1]:
            lowScoreIndex = i
    return pythonStudents[lowScoreIndex][1]
def removeLowScore(pythonStudents, lowScore):
    newArr = []
    for i in range (len(pythonStudents)):
            if pythonStudents[i][1] and pythonStudents[i][1] != lowScore:
                newArr.append(pythonStudents[i])
    return newArr
def findSameScore(pythonStudents, score):
    sameScoreName = []
    for i in range (len(pythonStudents)):
        if pythonStudents[i][1] == score:
            sameScoreName.append(pythonStudents[i][0])
    return sameScoreName
if __name__ == '__main__':
    pythonStudents = []
    N = int(input())
    for _ in range(N):
        name = input()
        score = float(input())
        pythonStudents.append([name, score])      
    lowestScore = findLowScore(pythonStudents)
    pythonStudentsEdited1 = removeLowScore(pythonStudents, lowestScore)
    
    secondLowestScore = findLowScore(pythonStudentsEdited1)
    
    sameScoreName = findSameScore(pythonStudentsEdited1, secondLowestScore)
    for name in sorted(sameScoreName):
        print(name)