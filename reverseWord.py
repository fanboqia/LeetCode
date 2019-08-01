class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        return " ".join(s.split()[::-1])
    
    """
    Solution2
    @param: s: A string
    @return: A string
    """
    def reverseWord(str):
        lStr = list(reversed(str))
        size = len(lStr)
        i = 0
        while i < size:
            j = 0
            while i < size and lStr[i] == ' ':
                i = i + 1
            while i + j < size and lStr[i + j] != ' ':
                j = j + 1
            lStr[i:i+j] = list(reversed(lStr[i:i+j]))
            i = i + j
        return "".join(lStr)
