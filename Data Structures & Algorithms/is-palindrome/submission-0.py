class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newS = ""
        revS = ""
        for i in s:
            if i.isalnum():
                newS += i

        revS = newS[::-1]

        return True if revS == newS else False