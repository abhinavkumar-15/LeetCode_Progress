class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  
        new = nums[-k:] + nums[:-k]
        nums[:] = new
