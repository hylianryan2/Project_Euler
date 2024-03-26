def is_prime(p):
    if p in [2, 3]:
        return True
    if p % 6 not in [1, 5]:
        return False
    for m in range(2, int(p**0.5) + 1):
        if p % m == 0:
            return False
    return True

def get_largest_prime_factor(n):
    for p in range(int(n**0.5), 1, -1):
        if is_prime(p) and n % p == 0:
            return p

print(get_largest_prime_factor(600_851_475_143))
