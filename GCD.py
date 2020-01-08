def gcd(a, b):
    m = min(a, b)
    for i in range(b):
        if a % m == 0 and b % m == 0:
            return i
        m -= 1

def uclid_gcd(a, b):
    if b is 0:
        return a
    return uclid_gcd(b, a % b)

print(gcd(60, 24))
print(uclid_gcd(60, 24))