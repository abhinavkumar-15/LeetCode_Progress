class Solution(object):
    def firstMissingPositive(self, nums):
        nums.sort()
        missing=1
        for num in nums:
            if num>0 and num == missing:
                missing+=1
        return missing