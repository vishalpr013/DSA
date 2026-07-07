class Solution(object):
    def isPalindrome(self, x):
        sign = 1
        if x<0:
            sign = -1
        ans = 0
        real = x
        x = abs(x)
        digit = 0
        while x!=0 :
            digit = x%10
            ans = ans*10 + digit
            x/=10
        return (ans == real)