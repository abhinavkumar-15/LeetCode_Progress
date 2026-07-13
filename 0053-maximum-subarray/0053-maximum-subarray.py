class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=nums[0]
        curr_max=nums[0]

        for i in range(1,len(nums)):
            curr_max=max(nums[i],nums[i]+curr_max)
            maximum=max(maximum, curr_max)

        return maximum
        