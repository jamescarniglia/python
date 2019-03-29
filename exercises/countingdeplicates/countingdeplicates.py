from collections import Counter
def duplicate_count(text):
    '''
    Write a function that will return the count of distinct case-insensitive alphabetic characters
    and numeric digits that occur more than once in the input string.
    The input string can be assumed to contain only alphabets
    (both uppercase and lowercase) and numeric digits.
    '''

     here = Counter(text.lower()).most_common()
     count=0
     for x, q in here:
         if q > 1:
             count+=1
     return count
