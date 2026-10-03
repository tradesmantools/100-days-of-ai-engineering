"""
Day 6/100 - Python Booleans and Truth Values Explained

bool - one of two values: True or False
     - a subclass of int (True == 1, False == 0)
     - every object has a truth value: bool(x) tells you what it is
     - falsy: False, None, 0, 0.0, Decimal("0"), "", [], {}, (), set()
     - everything else is truthy

Before running each section, write your predicted output in the comment.
"""
from decimal import Decimal

# --- 1. The bool type ---
# 1a. Print True, False                     # predict: True False
print(True, False)
# 1b. Print type(True)                      # predict: <class 'bool'>
print(type(True))
# 1c. Print True == 1, False == 0           # predict: True True
print(True == 1, False == 0)
# 1d. Print True + True                     # predict: 2
print(True + True)
# 1e. Print isinstance(True, int)           # predict: True
print(isinstance(True, int))
# 1f. Try print(true)                       # predict: NameError: name 'true' is not defined
# print(true)

# --- 2. Truthiness with bool() ---
# 2a. At the top of the file, add: from decimal import Decimal
# 2b. Print bool(0), bool(0.0), bool(42)          # predict: False False True
print(bool(0), bool(0.0), bool(42))
# 2c. Print bool(""), bool(" "), bool("False")    # predict: False True True
print(bool(""), bool(" "), bool("False"))
# 2d. Print bool([]), bool([0]), bool({})         # predict: False True False
print(bool([]), bool([0]), bool({}))
# 2e. Print bool(None)                            # predict: False
print(bool(None))
# 2f. Print bool(Decimal("0.00"))                 # predict: False
print(bool(Decimal("0.00")))
# 2g. Print bool("0")                             # predict: True  (non-empty string)
print(bool("0"))

# --- 3. Exercise: check a receipt line ---
# 3a. Set item = "  coffee beans  "
item = "  coffee beans  "
# 3b. Print bool(item), bool(item.strip())        # predict: True True
print(bool(item), bool(item.strip()))
# 3c. Set item = "   "
item = "   "
# 3d. Print bool(item), bool(item.strip())        # predict: True False  (spaces count until stripped)
print(bool(item), bool(item.strip()))
# 3e. Set qty_text = "0"   (text, as if typed by a user)
qty_text = "0"
# 3f. Print bool(qty_text)                        # predict: True   (text "0" is not empty)
print(bool(qty_text))
# 3g. Print bool(int(qty_text))                   # predict: False  (the number 0 is falsy)
print(bool(int(qty_text)))
# 3h. Set price = Decimal("0.00")
price = Decimal("0.00")
# 3i. Print bool(price)                           # predict: False
print(bool(price))
# 3j. Print bool(str(price))                      # predict: True   ("0.00" as text is not empty)
print(bool(str(price)))