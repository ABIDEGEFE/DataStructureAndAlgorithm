class Solution(object):
    def fib(self, n):
        fab = [0, 1]
        a, b = 0, 1
        
        for i in range(1, n):
            val = fab[a] + fab[b]
            fab.append(val)

            a += 1
            b += 1
        if n == 0:
            return 0
        return fab[-1]
        