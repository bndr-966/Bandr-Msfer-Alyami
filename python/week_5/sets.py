# Problem S1: Create and Add
# --------------------------
colors = {"red", "blue", "green"}
colors.add("yellow")
colors.add("red")  

print(f'Size of colors set: {len(colors)}')  
print(f'red in set: {"red" in colors}')
print(f'yellow in set: {"yellow" in colors}')


# --------------------------------------------
# Problem S2: Remove Duplicates from a List
# --------------------------------------------
nums = [1, 2, 2, 3, 4, 4, 5, 1]

unique_nums = set(nums)
print("Unique values:", unique_nums)
print("Count of unique values:", len(unique_nums))



# --------------------------
# Problem S3: Set Operations
# ---------------------------

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("In a but not in b:", a - b)