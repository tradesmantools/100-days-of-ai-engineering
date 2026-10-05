"""
Day 7/100 - Type Conversion in Python: Casting Between Data Types

implicit - Python converts for you, only when no data can be lost
           int + float -> float
explicit - you convert by calling the type: int(), float(), str(), Decimal(), list(), tuple()
         - each call returns a NEW object; the original is unchanged
         - converting text that doesn't fit the type raises ValueError
           (Decimal raises decimal.InvalidOperation instead)
         - mixing types Python won't convert for you raises TypeError

Before running each section, write your predicted output in the comment.
"""
from decimal import Decimal

# --- 1. Implicit conversion ---
# 1a. Print 1 + 2.0                          # predict: 3.0
print(1 + 2.0)
# 1b. Print type(1 + 2.0)                    # predict: <class 'float'>
print(type(1 + 2.0))
# 1c. Print 6 / 2                            # predict: 3.0  (/ always returns a float)
print(6 / 2)
# 1d. Try print("3" + 4)                     # predict: TypeError: can only concatenate str (not "int") to str
# print("3" + 4)

# --- 2. Converting to int ---
# 2a. Print int("42")                        # predict: 42
print(int("42"))
# 2b. Print int("  42  ")                    # predict: 42  (surrounding spaces are ignored)
print(int("  42  "))
# 2c. Print int(3.9)                         # predict: 3   (cuts off, does not round)
print(int(3.9))
# 2d. Print int(-3.9)                        # predict: -3  (cuts toward zero)
print(int(-3.9))
# 2e. Try print(int("3.5"))                  # predict: ValueError: invalid literal for int() with base 10: '3.5'
# print(int("3.5"))
# 2f. Print int(float("3.5"))                # predict: 3
print(int(float("3.5")))
# 2g. Try print(int("forty-two"))            # predict: ValueError: invalid literal for int() with base 10: 'forty-two'
# print(int("forty-two"))

# --- 3. Converting to float ---
# 3a. Print float("3.5")                     # predict: 3.5
print(float("3.5"))
# 3b. Print float(7)                         # predict: 7.0
print(float(7))
# 3c. Print float("1e3")                     # predict: 1000.0
print(float("1e3"))
# 3d. Print float("1.10") * 3                # predict: 3.3000000000000003
print(float("1.10") * 3)

# --- 4. Converting to str ---
# 4a. Print str(42) + str(42)                # predict: 4242
print(str(42) + str(42))
# 4b. Print str(3.0)                         # predict: 3.0
print(str(3.0))
# 4c. Print str(True)                        # predict: True  (the text "True", not the bool)
print(str(True))
# 4d. Print len(str(12345))                  # predict: 5
print(len(str(12345)))

# --- 5. Converting to Decimal ---
# 5a. At the top of the file, add: from decimal import Decimal
# 5b. Print Decimal("1.10") * 3              # predict: 3.30
print(Decimal("1.10") * 3)
# 5c. Print Decimal(1.10)                    # predict: 1.100000000000000088817841970012523233890533447265625
print(Decimal(1.10))                         # the float was already inexact; Decimal shows it exactly
# 5d. Try print(Decimal("1.10") + 1.5)       # predict: TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'float'
# print(Decimal("1.10") + 1.5)
# 5e. Try print(Decimal("ten"))              # predict: decimal.InvalidOperation: [<class 'decimal.ConversionSyntax'>]
# print(Decimal("ten"))

# --- 6. Converting between sequences ---
# 6a. Print list("abc")                      # predict: ['a', 'b', 'c']
print(list("abc"))
# 6b. Print tuple("abc")                     # predict: ('a', 'b', 'c')
print(tuple("abc"))
# 6c. Print "".join(list("abc"))             # predict: abc
print("".join(list("abc")))
# 6d. Print list(str(2026))                  # predict: ['2', '0', '2', '6']
print(list(str(2026)))

# --- 7. Exercise: build a receipt line from typed text ---
# 7a. Set item = "  coffee beans  ", qty_text = " 3 ", price_text = "1.10"
#     (all text, as if typed by a user)
item = "  coffee beans  "
qty_text = " 3 "
price_text = "1.10"
# 7b. Try print(price_text * qty_text)                          # predict: TypeError: can't multiply sequence by non-int of type 'str'
# print(price_text * qty_text)
# 7c. Set qty = int(qty_text) and price = Decimal(price_text)
qty = int(qty_text)
price = Decimal(price_text)
# 7d. Print type(qty), type(price)                              # predict: <class 'int'> <class 'decimal.Decimal'>
print(type(qty), type(price))
# 7e. Set total = price * qty
total = price * qty
# 7f. Print item.strip().title() + " x" + str(qty) + ": $" + str(total)   # predict: Coffee Beans x3: $3.30
print(item.strip().title() + " x" + str(qty) + ": $" + str(total))
# 7g. Set qty_text = "3.0"; try int(qty_text)                   # predict: ValueError: invalid literal for int() with base 10: '3.0'
qty_text = "3.0"
# int(qty_text)