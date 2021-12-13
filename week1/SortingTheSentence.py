class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        sortedArr = [0]*len(arr)
        order = [0]*len(arr)
        for i in range(len(arr)):
            order[i] = int(arr[i][-1])
            arr[i].replace(arr[i][-1],"")
        for i in range(len(arr)):
            sortedArr[order[i]-1] = arr[i][:-1]
        result = ' '.join(sortedArr)
        return result