class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        ans = -1
        sm = 0
        temp = x
        while x:
            sm+=x%10
            x/=10
        if temp%sm == 0:
            return sm
        return ans