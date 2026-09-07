class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        out=[]
        num_set=set(nums)
        n=len(nums)
        for i in range(1,n+1):
            if i not in num_set:
                out.append(i)
        return out
        """
        for num in nums:
            index = abs(num) -1
            nums[index] = -abs(nums[index])
        ans=[]
        for i in range(len(nums)):
            if nums[i]>0:
                ans.append(i+1)
        return ans
        