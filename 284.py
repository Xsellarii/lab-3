num = int(input())

if num == 0:
    print(0)
else:
    max_val = num
    count = 0

while True:
    num = int(input())
  
    if num == 0:
        break
    if num > max_val:
        max_val = num
        count = 1
    elif num == num == max_val:
        count += 1 

print(count)

