class Solution(object):
    def licenseKeyFormatting(self, s, k):

        formatted = s.split('-')
        form_str = ""
        
        form_str = "".join(formatted)
        
        rem = len(form_str)%k
        hasRem = False
        result = ""
        x = 0
        ix = 0
        for i in form_str:
            x += 1
            result += i.upper()
            rem -= 1
            if rem == 0 and len(s) != 1:
                result += "-"
                x = 0
            if x == k and ix < len(form_str)-1:
                result += "-"
                x = 0
            
            ix += 1
            
        return result
           


       
        