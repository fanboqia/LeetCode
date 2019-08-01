def sortLetters(chars):
    size = len(chars)
    i = 0
    j = size - 1
    lChars = list(chars)
    while i < j:
        while lChars[i].islower() and i < j:
            i = i + 1
        while lChars[j].isupper() and i < j:
            j = j - 1
        tmp = lChars[i]
        lChars[i] = lChars[j]
        lChars[j] = tmp
        i = i + 1
        j = j - 1
    return "".join(lChars)
