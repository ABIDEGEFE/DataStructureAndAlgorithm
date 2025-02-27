class Solution(object):
    def findRelativeRanks(self, score):
        s = {}
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        s_sorted = sorted(score, reverse=True)

        for i in range(len(score)):

            if len(s) > 2:
                break
            s[s_sorted[i]] = rank[i]

        ans = []
        for i in score:
            if i in s:
                ans.append(s[i])
            else:
                ans.append(str(s_sorted.index(i)+1))
        return ans
        