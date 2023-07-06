import string


def rotate(text, key):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    
    return text.translate(translation_table)