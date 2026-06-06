# Problem T1: Create and Access
# -----------------------------
person = ("Sara", 25, "Riyadh")

print("Name:", person[0])
print("Age:", person[1])
print("City:", person[2])



# Problem T2: Immutability Check
# ------------------------------

colors = ("red", "green", "blue")
try:
    colors[0] = "yellow"
except:    
    print("Length:", len(colors))
    print("red in tuple:", "red" in colors)

