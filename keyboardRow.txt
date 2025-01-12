class Solution(object):
    def findWords(self, words):
        result = []

        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"

        for word in words:
            fl = word[0].lower()
            if fl in r1:
                row = r1
            elif fl in r2:
                row = r2
            else:
                row = r3
            isFound = True
            for letter in word:
                if not letter.lower() in row:
                    isFound = False
                    break
            if isFound:
                result.append(word)
        
        return result

        
        