class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):

        td = 0
        for i in range(len(timeSeries)-1):
            td += min(timeSeries[i+1]-timeSeries[i], duration)
        return td+duration

        
        
        