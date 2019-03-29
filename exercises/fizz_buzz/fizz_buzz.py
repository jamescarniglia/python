#!/usr/local/bin/python

COUNTER = 100
MUL = {3 : 'FIZZ', 5 : 'BUZZ'}

def number_cruncher(counter,mul):
  """
  Takes a range to count up to and a dic of {number: "pharse"}
  iterates through count number and determines if the number in the dic
  is a muliplier.  If so prints  the phrase and not the number else prints
  number
  """
  # roll over counter
  while counter > 0:
    # setup list for append
    is_mul = []
    # roll over all keys in dic
    for x in mul.keys():
      # check if key is a mulitpler of counter
      if (counter % x == 0) :
        # if so append vaule to ins_mul
        is_mul.append(mul[x])
    # if a mulitplier is found print the list
    if is_mul:
      print(','.join(is_mul))
    else:
    # else just pring the counter
      print(counter)
    # descrese counter
    counter = counter-1

# run the function
number_cruncher(COUNTER,MUL)


