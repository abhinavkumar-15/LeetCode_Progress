class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        prefix=[0]*n
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i]
        pivot=-1
        for i in range(n):
            if i==0: left_sum=0
            else: left_sum=prefix[i-1]
            right_sum=prefix[-1]-prefix[i]
            if left_sum==right_sum:
                pivot=i
                break
        return pivot
        