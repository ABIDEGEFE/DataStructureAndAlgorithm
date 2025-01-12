class Solution(object):
    def subarraysDivByK(self, nums, k):

        d = {0 :1}
        count = total = 0

        for i in nums:
            total += i
            remainder = total % k

            if remainder < 0:
                remainder += k
            
            if remainder in d:
                count += d[remainder]
            
            d[remainder] = d.get(remainder, 0) + 1
        
        return count
        
        