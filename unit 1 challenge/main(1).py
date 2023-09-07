def fact(n):
  """This is a recursive function to find the factorial of an integer"""
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact(n-1)


number = 5
res = fact(number)
print("The factorial of {} is {}.".format(number,res))