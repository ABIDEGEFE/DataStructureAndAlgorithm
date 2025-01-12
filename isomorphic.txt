class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        ls1 = []
        ls2 = []

        zipped = zip(s, t)

        for i, j in list(zipped):
            if i in ls1:
                if ls2[ls1.index(i)] != j:
                    return False
                else:
                    ls1.append(i)
                    ls2.append(j)
            else:
                ls1.append(i)
                ls2.append(j)
            if j in ls2:
                if ls1[ls2.index(j)] != i:
                    return False
                else:
                    ls1.append(i)
                    ls2.append(j)
            else:
                ls1.append(i)
                ls2.append(j)
        return True
        