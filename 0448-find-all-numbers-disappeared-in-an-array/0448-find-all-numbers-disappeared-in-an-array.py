class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        out=[]
        num_set=set(nums)
        n=len(nums)
        for i in range(1,n+1):
            if i not in num_set:
                out.append(i)
        return out
        