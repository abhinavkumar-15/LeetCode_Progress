class Solution(object):
    def lengthOfLongestSubstring(self, s):

        st = set()
        left = 0
        maxi = 0

        for right in range(len(s)):

            while s[right] in st:
                st.remove(s[left])
                left += 1

            st.add(s[right])

            maxi = max(maxi, len(st))

        return maxi