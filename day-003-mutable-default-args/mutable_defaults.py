"""
Day 3/100 - Python interview question: the mutable default argument.

Interview question:
    What does this code print, and why?

        def add_item(item, items=[]):
            items.append(item)
            return items

        print(add_item("a"))
        print(add_item("b"))
"""


# --- 1. The bug -------------------------------------------------------------

def add_item(item, items=[]):
    items.append(item)
    return items


print("1. The bug")
print(add_item("a"))   # ['a']
print(add_item("b"))   # ['a', 'b']  <- surprise: expected ['b']


# --- 2. Proof: it's the SAME list every call ---------------------------------
# Python evaluates default values ONCE, when `def` runs, not on every call.
# The default list is stored on the function object itself.

print("\n2. The default lives on the function")
print(add_item.__defaults__)   # (['a', 'b'],)

first = add_item("c")
second = add_item("d")
print(first is second)         # True: both names point to one list object


# --- 3. Why ints don't have this problem ------------------------------------
# Follow-up interviewers ask: "Then why is this fine?"
# An int is immutable. `count += 1` creates a NEW int and rebinds the local
# name; the default object is never changed.

def increment(count=0):
    count += 1
    return count


print("\n3. Immutable default: no bug")
print(increment())  # 1
print(increment())  # 1


# --- 4. The fix: None as a sentinel ------------------------------------------

def add_item_fixed(item, items=None):
    if items is None:
        items = []     # new list created on EVERY call
    items.append(item)
    return items


print("\n4. The fix")
print(add_item_fixed("a"))  # ['a']
print(add_item_fixed("b"))  # ['b']