def iq_test(numbers):
    even = []
    odd  = []
    num_list = numbers.split(" ")
    for number in num_list:
      if int(number) % 2 == 0:
        even.append(number)
      else:
        odd.append(number)
    if len(odd) > 1:
      diff_num = "".join(even)
    else:
      diff_num = "".join(odd)

    return num_list.index(diff_num)+1
