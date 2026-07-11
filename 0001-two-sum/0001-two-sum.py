class Solution(object):
    def twoSum(self, nums, target):
        j=len(nums)-1
        out=[]
        for i in range(0,len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    out.append(i)
                    out.append(j)
                    break
                else:
                    j=j-1
        out=list(set(out))
        return out