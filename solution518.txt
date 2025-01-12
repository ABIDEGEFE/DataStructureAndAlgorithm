class Solution(object):
    def change(self, amount, coins):

        res = [0] * (amount + 1)
        res[0] = 1

        for coin in coins:
            for am in range(coin, len(res)):
                res[am] += res[am - coin]

        return res[-1]
        
        
        