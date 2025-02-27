class Solution(object):
    def maxCoins(self, piles):

      
        number_of_turn = len(piles)//3
        gap = 1
        count = 0
        piles = sorted(piles, reverse=True)
        while number_of_turn > 0:
            count += piles[gap]
            gap += 2
            number_of_turn -= 1
        return count
        