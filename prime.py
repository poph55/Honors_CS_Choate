num = int(input("Enter any number, and we will give all prime numbers lower than it (Including 1!)"))
factors = 0
div = 1

while div <= num:
  while factors < 3 and div <= num:
    if num%div == 0:
      factors = factors + 1
      div = div + 1
    else:
      div = div + 1
  if factors < 3:
    print(str(num))
    if num == 3 or num == 2:
      num = num - 1
    else:
      num = num-2
  elif num%2 == 0:
    num = num - 1
  else:
    num = num - 1  
  factors = 0
  div = 1