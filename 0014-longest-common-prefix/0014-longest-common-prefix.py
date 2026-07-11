class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = ""

        for i in range(len(strs[0])):

            for j in range(1, len(strs)):

                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return prefix

            prefix += strs[0][i]

        return prefix