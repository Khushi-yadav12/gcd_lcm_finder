def get_gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def get_lcm(a, b):
    if a == 0 or b == 0: return 0
    return abs(a * b) // get_gcd(a, b)

def simplify(n, d):
    common = get_gcd(n, d)
    return n // common, d // common

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def to_fraction(entry):
    entry = entry.strip().replace(" ", "") 
    
    if "/" in entry:
        parts = entry.split("/")
        n, d = int(parts[0]), int(parts[1])
        if d == 0: raise ZeroDivisionError("Denominator cannot be zero!")
        return simplify(n, d)
    
    elif "." in entry:
        decimal_places = len(entry.split(".")[1])
        denominator = 10 ** decimal_places
        numerator = int(entry.replace(".", ""))
        return simplify(numerator, denominator)
    
    else:
        return int(entry), 1

print("="*50)
print("             THE GCD & LCM CALCULATOR")
print("="*50)
print("Enter numbers separated by commas (e.g., 12, 0.5, 2/3)")

raw_input = input("\nEnter all numbers: ")

entries = raw_input.split(",")

nums_n = []
nums_d = []

for item in entries:
    try:
        n, d = to_fraction(item)
        nums_n.append(n)
        nums_d.append(d)
    except Exception as e:
        print(f"(!) Skipping '{item}': {e}")

if len(nums_n) < 2:
    print("\n(!) Error: You must provide at least two valid numbers.")
else:
    final_gcd_n, final_gcd_d = nums_n[0], nums_d[0]
    final_lcm_n, final_lcm_d = nums_n[0], nums_d[0]

    for i in range(1, len(nums_n)):
        final_gcd_n = get_gcd(final_gcd_n, nums_n[i])
        final_gcd_d = get_lcm(final_gcd_d, nums_d[i])
        
        final_lcm_n = get_lcm(final_lcm_n, nums_n[i])
        final_lcm_d = get_gcd(final_lcm_d, nums_d[i])

    gcd_n, gcd_d = simplify(final_gcd_n, final_gcd_d)
    lcm_n, lcm_d = simplify(final_lcm_n, final_lcm_d)

    print("\n" + "="*50)
    print("                  RESULTS ANALYSIS")
    print("-" * 50)

    primes = [n for n, d in zip(nums_n, nums_d) if d == 1 and is_prime(n)]
    if primes: print(f"Primes Found: {list(set(primes))}")

def output(n, d):
    if d == 1: return f"{n}"
    return f"{n}/{d} (approx {round(n/d, 4)})"

print(f"Final GCD: {output(gcd_n, gcd_d)}")
print(f"Final LCM: {output(lcm_n, lcm_d)}")
print("="*50)



