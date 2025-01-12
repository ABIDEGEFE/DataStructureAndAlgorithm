class Solution(object):
    def corpFlightBookings(self, bookings, n):

        answer = [0]*n

        for booking in bookings:

            answer[booking[0]-1] += booking[-1]

            if booking[1] < n:
                answer[booking[1]] -= booking[-1]

        for i in range(1, n):
            answer[i] += answer[i-1]
        
        return answer
      
        