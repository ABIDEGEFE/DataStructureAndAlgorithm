class Solution(object):
    def makesquare(self, matchsticks):
            
        if sum(matchsticks) % 4 != 0 or len(matchsticks) < 4:
            return False

        required_side = sum(matchsticks) // 4
        side = [0] * 4
        matchsticks.sort(reverse=True)

        def helper(index):
            if len(matchsticks) == index:
                return (sum(side) // 4) == required_side

            for i in range(4):
                if side[i] + matchsticks[index] > required_side:
                    continue

                side[i] += matchsticks[index]
                if helper(index + 1):
                    return True

                side[i] -= matchsticks[index]
                if side[i] == 0:
                    break

            return False
        return helper(0)
        