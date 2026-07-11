class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        count=0
        new=[]
        for i in range(n):
            if nums[i]!=0:
                new.append(nums[i])
            else:
                count+=1
        for i in range(count):
            new.append(0)
        nums[:] = new
        new=None