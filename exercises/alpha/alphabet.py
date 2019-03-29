#!/usr/local/sbin/python

def alphabet_position(text):
    alphabet = 'xabcdefghijklmnopqrstuvwxyz'
    result = []
    for letter in text:
        result.append(str(alphabet.index(letter)))
    return " ".join(result)



