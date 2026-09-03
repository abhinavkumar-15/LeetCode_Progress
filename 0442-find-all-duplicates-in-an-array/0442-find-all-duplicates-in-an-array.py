class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq={}
        out=[]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for k,v in freq.items():
            if v==2:
                out.append(k)
        return out
            
        