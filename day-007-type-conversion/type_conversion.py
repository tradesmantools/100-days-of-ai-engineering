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

# --- 1. Implicit conversion ---
# 1a. Print 1 + 2.0                          # predict:
# 1b. Print type(1 + 2.0)                    # predict:
# 1c. Print 6 / 2                            # predict:
# 1d. Try print("3" + 4)                     # predict:

# --- 2. Converting to int ---
# 2a. Print int("42")                        # predict:
# 2b. Print int("  42  ")                    # predict:
# 2c. Print int(3.9)                         # predict:
# 2d. Print int(-3.9)                        # predict:
# 2e. Try print(int("3.5"))                  # predict:
# 2f. Print int(float("3.5"))                # predict:
# 2g. Try print(int("forty-two"))            # predict:

# --- 3. Converting to float ---
# 3a. Print float("3.5")                     # predict:
# 3b. Print float(7)                         # predict:
# 3c. Print float("1e3")                     # predict:
# 3d. Print float("1.10") * 3                # predict:

# --- 4. Converting to str ---
# 4a. Print str(42) + str(42)                # predict:
# 4b. Print str(3.0)                         # predict:
# 4c. Print str(True)                        # predict:
# 4d. Print len(str(12345))                  # predict:

# --- 5. Converting to Decimal ---
# 5a. At the top of the file, add: from decimal import Decimal
# 5b. Print Decimal("1.10") * 3              # predict:
# 5c. Print Decimal(1.10)                    # predict:
# 5d. Try print(Decimal("1.10") + 1.5)       # predict:
# 5e. Try print(Decimal("ten"))              # predict:

# --- 6. Converting between sequences ---
# 6a. Print list("abc")                      # predict:
# 6b. Print tuple("abc")                     # predict:
# 6c. Print "".join(list("abc"))             # predict:
# 6d. Print list(str(2026))                  # predict:

# --- 7. Exercise: build a receipt line from typed text ---
# 7a. Set item = "  coffee beans  ", qty_text = " 3 ", price_text = "1.10"
#     (all text, as if typed by a user)
# 7b. Try print(price_text * qty_text)                          # predict:
# 7c. Set qty = int(qty_text) and price = Decimal(price_text)
# 7d. Print type(qty), type(price)                              # predict:
# 7e. Set total = price * qty
# 7f. Print item.strip().title() + " x" + str(qty) + ": $" + str(total)   # predict:
# 7g. Set qty_text = "3.0"; try int(qty_text)                   # predict: