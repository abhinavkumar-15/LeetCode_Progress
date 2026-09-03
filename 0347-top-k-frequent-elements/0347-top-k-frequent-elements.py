class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        arr = list(freq.items())
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j+1][1] > arr[j][1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        freq=dict(arr)
        arr=list(freq.keys())
        arr=arr[:k]
        return arr

        