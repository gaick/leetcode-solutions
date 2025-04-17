class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = [None] * (len(word1) + len(word2))
        i,j,k = 0,0,0
        while(i < len(word1) and j < len(word2)):
           result[k] = word1[i]
           k=k+1
           i=i+1
           result[k] = word2[j]
           k=k+1
           j=j+1
        while(i < len(word1)):
          result[k] = word1[i]
          k=k+1
          i=i+1
        while(j < len(word2)):
          result[k] = word2[j]
          k=k+1
          j=j+1
        return ''.join(result)
