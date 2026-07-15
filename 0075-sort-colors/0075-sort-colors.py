class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        n=len(nums)
        for i in range(0,n):
            for j in range(0,n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        """
        start, end, mid = 0 , len(nums)-1, 0
        while mid <= end:
            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums[start]
                mid += 1
                start += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
        """
        Do not return anything, modify nums in-place instead.
        """
        