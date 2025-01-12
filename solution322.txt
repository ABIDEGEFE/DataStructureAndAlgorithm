class Solution(object):
    def coinChange(self, coins, amount):

        res = [amount + 2] * (amount + 1)
        res[0] = 0

        for am in range(1, amount + 1):
            min_val = res[am]
            for coin in coins:
                if am - coin >= 0 and res[am - coin] < min_val:
                    min_val = res[am - coin] + 1

            res[am] = min_val
        if res[-1] > amount:
            return -1
        return res[-1]
       
       
        