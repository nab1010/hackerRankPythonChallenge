
def removeMaxNumber(arr, maxNumber):
    newArr = []
    for i in range (len(arr)):
        if arr[i] != maxNumber:
            newArr.append(arr[i])
    return newArr
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxNumber = max(arr)
    arr = removeMaxNumber(arr, maxNumber)
    runnerUpNumber = max(arr)
    print(runnerUpNumber)