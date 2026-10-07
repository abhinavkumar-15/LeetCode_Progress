class Solution(object):
    def findAnagrams(self, s, p):
        
        if len(p) > len(s):
            return []

        count_p = [0] * 26
        count_s = [0] * 26

        # Frequency of characters in p
        for ch in p:
            count_p[ord(ch) - ord('a')] += 1

        # First window
        for i in range(len(p)):
            count_s[ord(s[i]) - ord('a')] += 1

        result = []

        # Check first window
        if count_s == count_p:
            result.append(0)

        # Slide the window
        for i in range(len(p), len(s)):

            # Add new character
            count_s[ord(s[i]) - ord('a')] += 1

            # Remove old character
            count_s[ord(s[i - len(p)]) - ord('a')] -= 1

            # Check if current window is an anagram
            if count_s == count_p:
                result.append(i - len(p) + 1)

        return result