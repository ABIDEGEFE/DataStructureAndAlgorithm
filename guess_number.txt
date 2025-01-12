# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        higher = n
        lower = 1

        while True:

            mid = (higher+lower)//2
            response = guess(mid)

            if response == -1:
                higher = mid
            if response == 1:
                lower = mid + 1
            if response == 0:
                return mid
        