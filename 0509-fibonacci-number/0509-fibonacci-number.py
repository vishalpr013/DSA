class Solution(object):
    def fib(self, n):
        i,j = 0,1
        k = 0
        for i in range(n):
            i = j
            j = k
            k = i+j
        return k