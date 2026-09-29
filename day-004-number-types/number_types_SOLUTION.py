"""
Day 4/100 - Numbers in Python: Integers, Floats, and Complex Numbers

int     - whole numbers, no size limit, always exact
float   - decimals stored in binary, fast but approximate
complex - a real part plus an imaginary part, written with j
"""

import math
from decimal import Decimal


# --- 1. Integers are exact, no matter how big ------------------------------

big = 2 ** 100

print("1. Integers")
print(type(42))          # <class 'int'>
print(big)               # 1267650600228229401496703205376
print(big + 1 - big)     # 1 - still exact


# --- 2. Floats are approximate ----------------------------------------------
# 0.1 has no exact binary form, the same way 1/3 has no exact decimal form.

print("\n2. Floats")
print(type(3.5))                     # <class 'float'>
print(0.1 + 0.2)                     # 0.30000000000000004
print(0.1 + 0.2 == 0.3)              # False
print(math.isclose(0.1 + 0.2, 0.3))  # True - compare floats this way


# --- 3. Three kinds of division ----------------------------------------------

print("\n3. Division")
print(7 / 2)             # 3.5 - `/` always returns a float
print(7 // 2)            # 3   - floor division
print(-7 // 2)           # -4  - floors DOWN, not toward zero
print(7 % 2)             # 1   - remainder
print(divmod(7, 2))      # (3, 1) - both at once


# --- 4. Decimal for money (redoing the Day 1 calculator's math) -------------

price_float, quantity_float = 1.10, 3
price_dec, quantity_dec = Decimal("1.10"), Decimal("3")

print("\n4. Decimal")
print(price_float * quantity_float)  # 3.3000000000000003
print(price_dec * quantity_dec)      # 3.30
print(Decimal(0.1))                  # 0.1000000000000000055511151231257827...
print(Decimal("0.1"))                # 0.1 - build Decimals from strings


# --- 5. Complex numbers -----------------------------------------------------

z = 3 + 4j

print("\n5. Complex")
print(type(z))           # <class 'complex'>
print(z.real, z.imag)    # 3.0 4.0
print(abs(z))            # 5.0 - distance from zero (3-4-5 triangle)


# --- 6. Exercise: predict before running -------------------------------------

print("\n6. Exercise")
print(round(0.5), round(1.5), round(2.5))  # 0 2 2 - halves round to the even number