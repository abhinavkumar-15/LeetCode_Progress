class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        n=len(nums1)
        for i in range(n):
            for j in range(0,n-i-1):
                if nums1[j]>nums1[j+1]:
                    nums1[j],nums1[j+1]=nums1[j+1],nums1[j]
        print(nums1)
        if n%2==1:
            return nums1[n//2]
        else:
            return (nums1[n/2]+nums1[(n/2)-1])/2.0
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        