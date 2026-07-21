"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if curr_sum % k == 0:
                    count += 1

        return count
"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        mp = {0: 1}

        for num in nums:
            prefix += num
            rem = prefix % k

            if rem in mp:
                count += mp[rem]

            mp[rem] = mp.get(rem, 0) + 1

        return count