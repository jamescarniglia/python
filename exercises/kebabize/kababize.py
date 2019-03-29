def kebabize(string):
    '''
    Modify the kebabize function so that it converts a camel case string into a kebab case.
    '''
    just_alpha = ''.join([i for i in string if not i.isdigit()])
    if just_alpha == "":
      return just_alpha
    else:
      new_string=just_alpha[0].lower()
      for letter in just_alpha[1:]:
        if letter.isupper():
          new_string += '-'+letter.lower()
        else:
          new_string += letter
      return new_string
