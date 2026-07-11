class Solution(object):
    def searchRange(self, nums, target):
        out=[]
        n=len(nums)
        for i in range(n):
            if target==nums[i]:
                out.append(i)
                break
        else:
            out.append(-1)
        for i in range(n-1,-1,-1):
            if target==nums[i]:
                out.append(i)
                break
        else:
            out.append(-1)
        return out
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        