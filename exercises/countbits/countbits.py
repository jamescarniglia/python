def countBits(n):
 '''
 Write a function that takes an integer as input, and returns the number
 of bits that are equal to one in the binary representation of that number.
 You can guarantee that input is non-negative.
 '''
  n = bin(n)
  return sum(int(c) for c in n[2:].strip())
