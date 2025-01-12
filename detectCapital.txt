class Solution(object):
    def detectCapitalUse(self, word):
        if word.islower() or word.isupper() or word.istitle():
            return True
        return False
            
        
        