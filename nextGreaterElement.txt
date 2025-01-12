class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        ans = []

        for i in nums1:
            ix = nums2.index(i)
            y = len(ans)
            if ix+1 != len(nums2):
                c = i
                while ix < len(nums2)-1:
                    if c < nums2[ix+1]:
                        ans.append(nums2[ix+1])
                        break
                    ix += 1
                if y == len(ans):
                    ans.append(-1)
            else:
                ans.append(-1)
            
        return ans
     
        