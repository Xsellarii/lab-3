while True:
  n = input()

  if n == "":
    break

  n = int(n)

  total = 0
  for i in range(1, n):
    total += i * (i + 1)

  print(total)