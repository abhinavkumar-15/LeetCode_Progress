"""
from collections import Counter
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
        for ch,count in freq.items():
            for j in range(count):
                out+=ch
        
        return out

"""
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        chars = sorted(freq, key=lambda x: freq[x],reverse=True)
        res=[]
        for ch in chars:
            res.append(ch*freq[ch])
        return "".join(res)