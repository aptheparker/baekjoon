a = int(input())

for i in range(a):
  print(i*' ', end='')
  print((2*a - (2*i+1)) * '*')