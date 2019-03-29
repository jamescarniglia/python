import string, re

def alphabet_position(text):
    '''
    given a string, replace every letter with its position in the alphabet.
    '''
    alpha = string.ascii_lowercase
    lower_text = text.lower()
    punc_text = re.sub(r'[^\w\s]','',lower_text)
    no_space_text = re.sub('\s+','',punc_text)
    num = []
    if any(char.isdigit() for char in text):
        return ''
    else:
      for x in no_space_text:
        num.append((1+alpha.index(x)))
    return " ".join([str(i) for i in num])
