import math

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        len1 , len2= len(str1),len(str2)
        len_gcd = self.gcd(len1,len2)
        if len1 % len_gcd !=0 or len2 % len_gcd !=0 : return ""
        c =str1[:len_gcd]
        if all(str1[i:i+len_gcd]==c for i in range(0,len1,len_gcd)) and\
        all(str2[i:i+len_gcd]==c for i in range(0,len2,len_gcd)):
         return c
        return ""
    def gcd(self , a , b):
        return a if b == 0 else self.gcd(b,a%b)
