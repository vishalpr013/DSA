class Solution(object):
    def reverse(self, x):
        sign = 1
        if x<0:
            sign = -1
        ans = 0
        x = abs(x)
        digit = 0
        while x!=0 :
            digit = x%10
            ans = ans*10 + digit
            x/=10
        if not(-2**31 <= ans <= 2**31-1):
            return 0
        return ans*sign