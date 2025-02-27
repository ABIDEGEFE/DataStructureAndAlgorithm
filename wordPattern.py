class Solution(object):
    def wordPattern(self, pattern, s):


        pat = list(pattern)
        sl = s.split()
        if len(pat) != len(sl):
            return False
        dic = {}
        zipped = zip(pat, sl)

        for key, value in list(zipped):
            if not key in dic and not value in dic.values():
                dic[key] = value
            else:
                try:
                    if dic[key] != value:
                        return False
                except:
                    return False

        return True

        
        