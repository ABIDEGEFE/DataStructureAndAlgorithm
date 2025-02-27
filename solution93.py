class Solution(object):
    def restoreIpAddresses(self, s):

        if len(s) < 4 or len(s) > 12:
            return []

        result = []

        def helper(start, path):

            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            for i in range(1, 4):
                if start + i > len(s):
                    break
                if is_valid(s[start:start+i]):
                    path.append(s[start:start+i])
                    helper(start + i, path)
                    path.pop()

        def is_valid(segment):
            if segment[0] == "0" and len(segment) > 1:
                return False
            if int(segment) > 255:
                return False
            return True

        helper(0, [])
        return result
        
        