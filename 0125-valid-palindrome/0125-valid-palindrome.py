class Solution(object):
    def isPalindrome(self, s):
        s = "".join(char.lower() for char in s if char.isalnum())
        reverse = s[::-1]
        return reverse == s