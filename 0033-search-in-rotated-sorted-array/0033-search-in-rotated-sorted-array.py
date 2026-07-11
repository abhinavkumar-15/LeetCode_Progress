class Solution(object):
    def search(self, nums, target):
        if target not in nums:
            return -1
        for i in range(0,len(nums)):
            if nums[i]==target:
                return i
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        