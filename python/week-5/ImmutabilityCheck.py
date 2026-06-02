colors = ("red", "green", "blue")

try:
    colors[0] = "yellow"
except TypeError as e:
    print(f"Error caught (as expected): {e}")

print(f"Length: {colors.__len__()}")
print(f"red in tuple: {'red' in colors}")
