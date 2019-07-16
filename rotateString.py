class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        if len(s) == 0:
            return s
        if offset == len(s):
            return s
        elif offset > len(s):
            offset = offset%len(s)
        p1 = s[len(s)-offset:]
        p2 = s[:len(s)-offset]
        s[:len(s)-offset] = p1
        s[len(s)-offset:] = p2
        return s
