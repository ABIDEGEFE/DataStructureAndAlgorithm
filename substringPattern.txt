class Solution(object):
    def repeatedSubstringPattern(self, s):
    
        pattern = ""

        for i in s:
            pattern += i
            if s.count(pattern)*len(pattern) == len(s) and pattern != s:
                return True
        return False