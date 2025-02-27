class Solution(object):
    def intersect(self, nums1, nums2):
        isNum2 = False
        ans = []

        if len(nums1) > len(nums2):
            isNum2 = True

        if isNum2:
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    nums1.remove(nums2[i])
                    ans.append(nums2[i])
        else:
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    nums2.remove(nums1[i])
                    ans.append(nums1[i])

        return ans

        