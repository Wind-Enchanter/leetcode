class Solution:
    def no_space(self,s: str)->str:
        # s = " ".join(s)
        out = ""
        i = 0
        while i < len(s):
            if s[i] == " " and s[i-1] != " ":
                j = i+1
                while s[j]==" ":
                    j+=1
                # s[i:j] = " "
                i = j-1
            out += s[i]
            i += 1
        return out

    def reverseWords(self, s: str) -> str:
        words = self.no_space(s)
        words = words.strip(" ").split(" ")
        out = ""
        for i in range(len(words)-1,-1,-1):
            if words[i] != " ":
                out += words[i]
                out += " "
        return out.strip(" ")


if __name__=="__main__":
    my_so = Solution()
    temp = "a good   example"
    res = my_so.reverseWords(temp)
    print(str(res))


