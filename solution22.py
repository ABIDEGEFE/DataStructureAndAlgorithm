class Solution(object):
    def generateParenthesis(self, n):
            
        res = []

        def helper(current_comb, open_part, close_part):
            if len(current_comb) == 2 * n:
                res.append(current_comb)
                return

            if open_part < n:
                helper(current_comb + "(", open_part + 1, close_part)

            if close_part < open_part:
                helper(current_comb + ")", open_part, close_part + 1)
                
        helper("", 0, 0)
        return res
        