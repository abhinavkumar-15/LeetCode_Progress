class Solution(object):
    def lengthOfLastWord(self, s):
        s=s[::-1]
        w=""
        s=s.strip()
        for i in range(len(s)):
            if s[i]==" ": break
            w+=s[i]
        return len(w)

            
        """
        :type s: str
        :rtype: int
        """
        