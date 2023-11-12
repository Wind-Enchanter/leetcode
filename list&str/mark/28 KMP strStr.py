class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length_h = len(haystack)
        length_n = len(needle)
        if(length_n==0):
            result = 0
        else:
            next = self.generte_next_in_KMP(needle)
            h=0
            n=0
            while(h<length_h and n<length_n):
                if(n==-1 or haystack[h]==needle[n]):
                    h=h+1
                    n=n+1
                else:
                    n= next[n]  #back to the position
            if(n==length_n):
                result = h - length_n
            else:
                result = -1
        return result
    def generte_next_in_KMP(self, s):
        """
        :type s: str
        :rtype: str
        """
        # next[i] = s[:i] 的前后缀(不包括本身)的最长公共子缀的长度

        length = len(s)
        j = 0

        next = [0 for i in range(length)]
        t = -1
        next[j] = t

        while (j < length - 1):
            if (0 > t):
                j = j + 1  # j=1
                t = t + 1  # t=0
                next[j] = t  # next[1]=0
            elif (s[j] == s[t]):
                j = j + 1
                t = t + 1
                next[j] = t
            else:
                t = next[t]  # ???crazy
        return next