class Solution(object):
    def reverseVowels(self, s):

        vowel_set = {'a', 'o', 'i', 'e', 'u','A','E','I','O','U'}
        left = 0
        right = len(s)-1
        s = list(s)
        while left < right:

            if not s[left] in vowel_set:
                left += 1
            if not s[right] in vowel_set:
                right -= 1
            if s[left]  in vowel_set and s[right] in vowel_set:
                temp = s[right]
                s[right] = s[left]
                s[left] = temp
                left += 1
                right -= 1
        return "".join(s)
        