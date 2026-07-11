class Solution(object):
    def strStr(self, haystack, needle):
        k=len(needle)-1
        for i in range(len(haystack)-k):
            if haystack[i:i+k+1]==needle:
                return i
        else:
            return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        