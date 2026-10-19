from pyinputplus import inputInt
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def goldbach_partitions(n):
    partitions = []
    if n % 2 != 0 or n < 4:
        return []
    for i in range(2, n//2 + 1):
        if is_prime(i) and is_prime(n-i):
            partitions.append(f"{i}+{n-i}")
    return partitions
n = inputInt('Partitions {p1 + p2} to look for the Number: ', max=3000, min=3)
print(goldbach_partitions(n))
