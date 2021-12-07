target = 25
prompt = 'What is the square root of %s?\n' % target
g = input(prompt)
threshold = .000005

approx = g * g

if (__name__ == '__main__'):

  while (approx <= target):
    # Moar iterations...
    if (g < target):
      g += threshold
    else:
      g -= threshold
    approx = g * g
    print('g is now:', g)
    print('g * g =', g * g)
    print('approx is now:', approx)

  print ('Solution is: ', g)
