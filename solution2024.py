class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        
        def helper(target):

            oper = k
            ix = left = max_length =  0

            for right in range(len(answerKey)):

                if answerKey[right] != target:
                    oper -= 1
                while oper < 0:
                    if answerKey[left] != target:
                        oper += 1
                    left += 1

                max_length = max(max_length, right-left+1)

            return max_length

        return max(helper("T"), helper("F"))

        
        