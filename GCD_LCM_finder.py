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

print("="*40)
print("GCD & LCM CALCULATOR")
print("="*40)
print("Instructions:")
print("Enter integers (e.g., 34)")
print("Enter fractions (e.g., 3/4)")
print("Enter 'done' to calculate.")

nums_top = []
nums_bottom = []

while True:
  entry = input("\nEnter value:").strip().lower()

  if entry == 'done':
    if len(nums_top) < 2:
      print("(!) Please enter at least two numbers to compare.")
      continue
    break

  if "/" in entry:
    try:
      n, d = map(int, entry.split("/"))
      if d == 0:
        print("(!) Error: Denominator cannot be zero.")
        continue
      nums_top.append(n)
      nums_bottom.append(d)
    except ValueError:
      print("(!) Error: Invalid fraction format. Use 'numerator/denominator' (e.g. 3/4)")
  
  elif entry.replace("-", "").isdigit():
    nums_top.append(int(entry))
    nums_bottom.append(1)
  else:
    print("(!) Error: Invalid input. Please enter an whole number or a fraction.")

res_gcd_n, res_gcd_d = nums_top[0], nums_bottom[0]
res_lcm_n, res_lcm_d = nums_top[0], nums_bottom[0]

for i in range(1, len(nums_top)):
  res_gcd_n = get_gcd(res_gcd_n, nums_top[i])
  res_gcd_d = get_lcm(res_gcd_d, nums_bottom[i])

  res_lcm_n = get_lcm(res_lcm_n, nums_top[i])
  res_lcm_d = get_gcd(res_lcm_d, nums_bottom[i])

final_gcd_n, final_gcd_d = simplify(res_gcd_n, res_gcd_d)
final_lcm_n, final_lcm_d = simplify(res_lcm_n, res_lcm_d)

print("\n" + "-"*40)
print("ANALYSIS RESULTS")
print("-"*40)

primes = [n for n, d in zip(nums_top, nums_bottom) if d == 1 and is_prime(n)]
if primes:
  print(f"Prime Numbers Found: {list(set(primes))}")

gcd_out = f"{final_gcd_n}" if final_gcd_d == 1 else f"{final_gcd_n}/{final_gcd_d}"
print(f"Greatest Common Divisor (GCD): {gcd_out}")

lcm_out = f"{final_lcm_n}" if final_lcm_d == 1 else f"{final_lcm_n}/{final_lcm_d}"
print(f"Least Common Multiple (LCM): {lcm_out}")
print("-"*40)




