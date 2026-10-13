n = int(input())

positive_count = 0
negative_count = 0
zero_count = 0

for _ in range(n):
    num = int(input())
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1
  
print(positive_count, negative_count, zero_count)
    