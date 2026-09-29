"""
Day 5/100 - Working with Strings in Python

str - an immutable sequence of characters
      - create with '', "", or triple quotes
      - index and slice like a list, but you can't change it in place
      - every "change" returns a new string

Before running each section, write your predicted output in the comment.
Lines marked "Try" raise an error on purpose: run once, see the error, then comment them out.
"""

# --- 1. Creating strings ---
# 1a. Set single = 'hello' and double = "hello"
# 1b. Print single == double                 # predict:
# 1c. Print type(single)                     # predict:
# 1d. Print "It's fine"                      # predict:
# 1e. Print 'She said "hi"'                  # predict:
# 1f. Print 'It\'s escaped'                  # predict:
# 1g. Print "line one\nline two"             # predict:
# 1h. Print "tab\there"                      # predict:
# 1i. Set poem = """roses
#     are red"""  (the second line flush left, no indent)
#     Print poem                             # predict:
# 1j. Print len("hello"), len(""), len("\n") # predict:

# --- 2. Indexing ---
# 2a. Set word = "Python"
# 2b. Print word[0]          # predict:
# 2c. Print word[5]          # predict:
# 2d. Print word[-1]         # predict:
# 2e. Print word[-6]         # predict:
# 2f. Try print(word[6])     # predict:

# --- 3. Slicing ---
# 3a. Print word[0:2]        # predict:
# 3b. Print word[2:]         # predict:
# 3c. Print word[:2]         # predict:
# 3d. Print word[-3:]        # predict:
# 3e. Print word[0:100]      # predict:
# 3f. Print word[::2]        # predict:
# 3g. Print word[::-1]       # predict:

# --- 4. Strings are immutable ---
# 4a. Try word[0] = "J"                         # predict:
# 4b. Set new_word = "J" + word[1:]; print it   # predict:
# 4c. Print word                                # predict:

# --- 5. Basic methods (each returns a NEW string) ---
# 5a. Set name = "  jon  "
# 5b. Print name.upper()             # predict:
# 5c. Print name.strip()             # predict:
# 5d. Print name.strip().title()     # predict:
# 5e. Print "a-b-c".replace("-", "+")  # predict:
# 5f. Print "a,b,c".split(",")       # predict:
# 5g. Print "-".join(["a", "b", "c"])  # predict:
# 5h. Print "th" in "Python"         # predict:

# --- 6. Exercise: print a receipt line ---
# 6a. At the top of the file, add: from decimal import Decimal
# 6b. Set item = "  coffee beans  " and total = Decimal("1.10") * Decimal("3")
# 6c. Try print("Total: $" + total)                        # predict:
# 6d. Print item.strip().title() + ": $" + str(total)      # predict: