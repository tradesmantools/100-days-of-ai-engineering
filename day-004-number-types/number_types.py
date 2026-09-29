"""
Day 4/100 - Numbers in Python: Integers, Floats, and Complex Numbers

int     - whole numbers, no size limit, always exact
float   - decimals stored in binary, fast but approximate
complex - a real part plus an imaginary part, written with j

Before running each section, write your predicted output in the comment.
"""

# 0. Import math, and Decimal from the decimal module
import math
from decimal import Decimal

# --- 1. Integers are exact, no matter how big ---
# 1a. Set big = 2 ** 100
# 1b. Print type(42)         # predict: int
# 1c. Print big              # predict: 1267650600228229401496703205376
# 1d. Print big + 1 - big    # predict: 1

# --- 2. Floats are approximate ---
# 2a. Print type(3.5)                     # predict: float
# 2b. Print 0.1 + 0.2                     # predict: 0.30000000000000000
# 2c. Print 0.1 + 0.2 == 0.3              # predict: False
# 2d. Print math.isclose(0.1 + 0.2, 0.3)  # predict: True

# --- 3. Three kinds of division ---
# 3a. Print 7 / 2            # predict: 3.5
# 3b. Print 7 // 2           # predict: 3
# 3c. Print -7 // 2          # predict: -4
# 3d. Print 7 % 2            # predict: 1
# 3e. Print divmod(7, 2)     # predict: (3, 1)

# --- 4. Decimal for money (redo the Day 1 calculator's math) ---
# 4a. Set price_float = 1.10 and quantity_float = 3
# 4b. Set price_dec = Decimal("1.10") and quantity_dec = Decimal("3")
# 4c. Print price_float * quantity_float   # predict: 3.3000000000000003
# 4d. Print price_dec * quantity_dec       # predict: 3.30
# 4e. Print Decimal(0.1)                   # predict: 0.1000000000000000055511151231257827...
# 4f. Print Decimal("0.1")                 # predict: 0.1

# --- 5. Complex numbers ---
# 5a. Set z = 3 + 4j
# 5b. Print type(z)          # predict: complex
# 5c. Print z.real, z.imag   # predict: 3.0 4.0
# 5d. Print abs(z)           # predict: 5.0

# --- 6. Exercise ---
# 6a. Print round(0.5), round(1.5), round(2.5)   # predict: 0 2 2