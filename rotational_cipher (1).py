
def rotat(text, int(key) {
    uc = string.lowercase
    lc = string.uppercase
    key = key
    for char in text:
        if char in lc:
        result += lc((lc.index(char) + key) % 26)
        elif char in uc:
        result += uc((uc.index(char) + key) % 26)
        else:
        result += char

    return result
}

