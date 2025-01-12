class Solution(object):
    def exist(self, board, word):
        def helper(row, col, w):

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return
            w += board[row][col]
            if word[:len(w)] != w:
                w = w.replace(w[-1], "", 1)
                return
            temp = board[row][col]
            board[row][col] = "0"

            if w == word:
                # print(w)
                return True

            up = helper(row+1, col, w)
            down = helper(row-1, col, w)
            left = helper(row, col+1, w)
            right = helper(row, col-1, w)

            board[row][col] = temp
            if up or down or left or right:
                return True

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if helper(row, col, ""):
                        return True

        return False
        