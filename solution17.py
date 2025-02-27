class Solution(object):
    def letterCombinations(self, digits):

        if not digits:
            return []
      
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []

        def helper(index, comb):
            if len(comb) == len(digits):
                res.append("".join(comb))
                return

            cur_letter = d[digits[index]]

            for letter in cur_letter:
                comb.append(letter)
                helper(index + 1, comb)
                comb.pop()

        helper(0, [])
        return res
        