class Solution(object):
    def reverse(self, x):
        x=str(x)
        if x[0]=="-":
            y=x[1::]
            y=y[::-1]
            if int(y)>(2**31)-1: return 0
            return int(y)*-1
        else:
            x=x[::-1]
            if int(x)>(2**31)-1: return 0
            return int(x)
        """
        :type x: int
        :rtype: int
        """
        