class Solution(object):
    def isValid(self, s):
        stack=[]
        if len(s)%2==1: return False
        for ch in s:
            if ch=="(" or ch=="{" or ch=="[":
                stack.append(ch)
            elif ch==")" or ch=="}" or ch=="]":
                if not stack: return False
                var=stack.pop()
                if (var=="(" and ch==")") or (var=="{" and ch=="}") or (var=="[" and ch=="]") : continue
                else: return False
        return len(stack)==0
        """
        :type s: str
        :rtype: bool
        """