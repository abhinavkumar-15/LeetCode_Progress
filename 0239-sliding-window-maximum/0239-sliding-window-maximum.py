"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        out=[]
        max_var=0
        l=0
        r=k-1
        for i in range(len(nums)-k+1):
            max_var=nums[l]
            for j in range(l+1,r+1):
                if nums[j]>max_var:
                    max_var=nums[j]
            out.append(max_var)
            l+=1
            r+=1
        return out
"""
"""
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
"""
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        res = []

        for i in range(len(nums)):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res