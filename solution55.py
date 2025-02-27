class Solution(object):
    def merge(self, intervals):
       
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals)
        res = [intervals[0]]

        for i in range(1, len(intervals)):

            if intervals[i][0] <= res[-1][1]:
                if intervals[i][1] > res[-1][1]:
                    res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])

        return res
        