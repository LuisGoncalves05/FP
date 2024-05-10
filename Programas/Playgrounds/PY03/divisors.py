num = int(input())
divisors = []
sum_of_divisors = 0

for _ in range (1, num+1):
    if num % _ == 0:
        divisors.append(_)

for i in divisors:
    sum_of_divisors += i

print(sum_of_divisors)
