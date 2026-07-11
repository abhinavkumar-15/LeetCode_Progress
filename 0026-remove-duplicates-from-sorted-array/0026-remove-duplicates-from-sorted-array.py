class Solution(object):
    def removeDuplicates(self, nums):
        new=[]
        k=len(nums)
        for i in range(k):
            if nums[i] not in new:
                new.append(nums[i])
            else:
                nums[i]="_"
        k=len(new)
        nums.sort()
        return k