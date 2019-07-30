"""
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        if source == "" and target == "":
            return 0
        i = 0
        tLen = len(target)
        sLen = len(source)
        while i < sLen:
            isMatch = False
            j = 0
            while i+j < sLen and j < tLen and target[j] == source[i+j]:
                j = j + 1
            if j == tLen:
                return i
            i = i + 1
        return -1  
