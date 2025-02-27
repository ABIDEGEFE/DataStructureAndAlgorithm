class Solution(object):
    def firstUniqChar(self, s):
        
        for i in s:
            first = s.find(i)
            last = s.rfind(i)

            if first == last:
                return first
            
        return -1


        