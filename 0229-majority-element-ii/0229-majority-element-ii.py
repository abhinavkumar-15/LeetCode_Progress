class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        times=n//3
        freq={}
        out=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for keys,values in freq.items():
            if values>times:
                out.append(keys)
        return out

        