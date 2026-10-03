"""
Day 6/100 - Python Booleans and Truth Values Explained

bool - one of two values: True or False
     - a subclass of int (True == 1, False == 0)
     - every object has a truth value: bool(x) tells you what it is
     - falsy: False, None, 0, 0.0, Decimal("0"), "", [], {}, (), set()
     - everything else is truthy

Before running each section, write your predicted output in the comment.
"""

# --- 1. The bool type ---
# 1a. Print True, False                     # predict:
# 1b. Print type(True)                      # predict:
# 1c. Print True == 1, False == 0           # predict:
# 1d. Print True + True                     # predict:
# 1e. Print isinstance(True, int)           # predict:
# 1f. Try print(true)                       # predict:

# --- 2. Truthiness with bool() ---
# 2a. At the top of the file, add: from decimal import Decimal
# 2b. Print bool(0), bool(0.0), bool(42)          # predict:
# 2c. Print bool(""), bool(" "), bool("False")    # predict:
# 2d. Print bool([]), bool([0]), bool({})         # predict:
# 2e. Print bool(None)                            # predict:
# 2f. Print bool(Decimal("0.00"))                 # predict:
# 2g. Print bool("0")                             # predict:

# --- 3. Exercise: check a receipt line ---
# 3a. Set item = "  coffee beans  "
# 3b. Print bool(item), bool(item.strip())        # predict:
# 3c. Set item = "   "
# 3d. Print bool(item), bool(item.strip())        # predict:
# 3e. Set qty_text = "0"   (text, as if typed by a user)
# 3f. Print bool(qty_text)                        # predict:
# 3g. Print bool(int(qty_text))                   # predict:
# 3h. Set price = Decimal("0.00")
# 3i. Print bool(price)                           # predict:
# 3j. Print bool(str(price))                      # predict: