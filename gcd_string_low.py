class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        c = self.gdc(len(str1),len(str2))
        return str1[:c]

        
    def gdc(self, a ,b):
        while b:
            a,b = b,a % b
        return a
