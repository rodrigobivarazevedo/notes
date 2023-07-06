def convert(s):

    return [s[:i] + s[i].upper() + s[i+1:] if s[i].isalpha() else s for i in range(len(s))]
