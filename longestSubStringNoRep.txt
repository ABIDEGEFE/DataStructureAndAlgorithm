class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        count = 0
        subS = ""
        prev = ""
        while count < len(s):
            if not s[count] in subS:
                subS += s[count]
            else:
                if len(subS) > len(prev):
                    prev = subS
                ix = s.index(s[count])
                subS = ""
                s = s[ix+1:]
                count = 0
                continue
            count += 1
        if len(subS) > len(prev):
            return len(subS)
        return len(prev)



      

        
        