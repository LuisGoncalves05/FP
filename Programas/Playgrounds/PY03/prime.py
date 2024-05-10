lower = int(input())
upper = int(input())
primes = []
primes_to_print = ""

def is_prime (number):
    if number > 1:
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True

for i in range(lower, upper+1):
    if is_prime(i):
        primes.append(i)

for prime in primes:
    primes_to_print += str(prime) + " "

print(f"Prime numbers between {lower} and {upper} are:", primes_to_print)