def alphabet_position(text):
    alphabet = 'xabcdefghijklmnopqrstuvwxyz'
    result = []
    for letter in text:
        if letter.isalpha():
            result.append(str(alphabet.index((letter.lower()))))
    return " ".join(result)

