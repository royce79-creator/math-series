def fibonacci(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1 
  elif n > 2: 
    return fibonacci(n - 1) + fibonacci(n - 2)
'''
In the sequence above you'll be taking in the (nth) term and add the values of those squecnes together.
'''
def lucas(n):
  if n == 0:
    return 2
  if n == 1: 
    return 1
  else:
    return lucas(n - 1) + lucas(n - 2)
'''
Above if n == 0 then it will always return 2 and if n == 1 then it will always return 1. If not then it will return the nth number and add the values up after subtracting 1 and 2 from the values spereately.
'''

def sum_series(n, param1 = 0, param2 = 1):
  if param1 == 0 and param2 == 1:
    return fibonacci(n)
  elif param1 == 2 and param2 == 1:
    return lucas(n)   
  if n == 0:
    return 2
  if n == 1:
    return 1
  if n == 2:
    return 1
  elif n > 2:
    return sum_series(n - 1, param1, param2) + sum_series(n - 2, param1, param2)
'''
In the above function there is a fucntion called sum_series that has a mandatory parameter followed by two optional parameters. in this it shows if param1 and param2 have limitation to what they are assigned to and if they are the values above then they will either return the fibonacci or lucas functions. Below that is a comobnation of the fibonacci and lucas function rules that will provide an output that works for either. 
'''


