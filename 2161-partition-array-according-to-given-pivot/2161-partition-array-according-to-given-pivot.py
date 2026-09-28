class Solution(object):
    def pivotArray(self, nums, pivot):
        left=[]
        piv=[]
        right=[]
        for i in nums:
            if i<pivot:
                left.append(i)
            elif i==pivot:
                piv.append(i)
            else:
                right.append(i)
        left.extend(piv)
        left.extend(right)
        return left
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        