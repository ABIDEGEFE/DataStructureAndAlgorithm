class Solution(object):
    def findContentChildren(self, g, s):
        
        outPut = 0
        while 0 < len(s):
            
            Smin = min(s)
            if len(g)>0:
                Gmin = min(g)

                if Smin >= Gmin:
                    outPut += 1
                    g.remove(Gmin)
            s.remove(Smin)
        return outPut

        
        