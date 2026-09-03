#from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        out=""
        arr=list(freq.items())
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j][1] < arr[j + 1][1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        freq=dict(arr)
        print(freq)
        for num,count in freq.items():
            for j in range(count):
                out+=num
        
        return out

        