class Solution(object):
    def minimumLength(self, s):
        while len(s) > 1 and s[0] == s[-1]:
            n = len(s)

            i = 0
            while i < n and s[i] == s[0]:
                i += 1

            j = n - 1
            while j >= i and s[j] == s[0]:
                j -= 1

            s = s[i:j+1]

        return len(s)