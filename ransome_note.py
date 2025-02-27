class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        outPut = ""
        for i in ransomNote:
            if i in magazine:
                outPut += i
                magazine = magazine.replace(i, " ", 1)

        if ransomNote == outPut:
            return True
        return False

        