"""
Day 5/100 - Working with Strings in Python

str - an immutable sequence of characters
      - create with '', "", or triple quotes
      - index and slice like a list, but you can't change it in place
      - every "change" returns a new string

Before running each section, write your predicted output in the comment.
"""
from decimal import Decimal

# --- 1. Creating strings ---
# 1a. Set single = 'hello' and double = "hello"
single = 'hello'
double = "hello"

# 1b. Print single == double                 # predict: True
print(single == double)

# 1c. Print type(single)                     # predict: <class 'str'>
print(type(single))

# 1d. Print "It's fine"                      # predict: It's fine
print("It's fine")

# 1e. Print 'She said "hi"'                  # predict: She said "hi"
print('She said "hi"')

# 1f. Print 'It\'s escaped'                  # predict: It's escaped
print('It\'s escaped')

# 1g. Print "line one\nline two"             # predict: line one
#                                           #          line two
print("line one\nline two")

# 1h. Print "tab\there"                      # predict: tab<TAB>here
print("tab\there")

# 1i. Print poem                             # predict: roses
#                                           #          are red
poem = """roses
are red"""
print(poem)

# 1j. Print len("hello"), len(""), len("\n") # predict: 5 0 1
print(len("hello"), len(""), len("\n"))

# --- 2. Indexing ---
# 2a. Set word = "Python"
word = "Python"
# 2b. Print word[0]          # predict: P
print(word[0])
# 2c. Print word[5]          # predict: n
print(word[5])
# 2d. Print word[-1]         # predict: n
print(word[-1])
# 2e. Print word[-6]         # predict: P
print(word[-6])
# 2f. Try print(word[6])          # predict: IndexError: string index out of range
# print(word[6])             # IndexError: string index out of range

# --- 3. Slicing ---
# 3a. Print word[0:2]        # predict: Py
print(word[0:2])
# 3b. Print word[2:]         # predict: thon
print(word[2:])
# 3c. Print word[:2]         # predict: Py
print(word[:2])
# 3d. Print word[-3:]        # predict: hon
print(word[-3:])
# 3e. Print word[0:100]      # predict: Python
print(word[0:100])
# 3f. Print word[::2]        # predict: Pto
print(word[::2])
# 3g. Print word[::-1]       # predict: nohtyP
print(word[::-1])

# --- 4. Strings are immutable ---
# 4a. Try word[0] = "J"                         # predict: TypeError: 'str' object does not support item assignment
# word[0] = "J"              # TypeError: 'str' object does not support item assignment
# 4b. Set new_word = "J" + word[1:]; print it   # predict: Jython
new_word = "J" + word[1:]
print(new_word)
# 4c. Print word                                # predict: Python
print(word)

# --- 5. Basic methods (each returns a NEW string) ---
# 5a. Set name = "  jon  "
name = "  jon  "
# 5b. Print name.upper()             # predict: |  JON  |
print("|" + name.upper() + "|")
# 5c. Print name.strip()             # predict: jon
print(name.strip())
# 5d. Print name.strip().title()     # predict: Jon
print(name.strip().title())
# 5e. Print "a-b-c".replace("-", "+")  # predict: a+b+c
print("a-b-c".replace("-", "+"))
# 5f. Print "a,b,c".split(",")       # predict: ['a', 'b', 'c']
print("a,b,c".split(","))
# 5g. Print "-".join(["a", "b", "c"])  # predict: a-b-c
print("-".join(["a", "b", "c"]))
# 5h. Print "th" in "Python"         # predict: True
print("th" in "Python")

# --- 6. Exercise: print a receipt line ---
# 6a. At the top of the file, add: from decimal import Decimal
# 6b. Set item = "  coffee beans  " and total = Decimal("1.10") * Decimal("3")
item = "  coffee beans  "
total = Decimal("1.10") * Decimal("3")
# 6c. Try print("Total: $" + total)                        # predict: TypeError: can only concatenate str (not "Decimal") to str
# print("Total: $" + total)
# 6d. Print item.strip().title() + ": $" + str(total)      # predict: Coffee Beans: $3.30
print(item.strip().title() + ": $" + str(total))           # Coffee Beans: $3.30