# Multiplication table of 5

# Method 1: Using a for loop
print("Multiplication Table of 5:")
print("-" * 25)
for i in range(1, 11):
    result = 5 * i
    print(f"5 × {i} = {result}")

print("\n" + "-" * 25)

# Method 2: Using a while loop (alternative)
print("\nAlternative using while loop:")
print("-" * 25)
i = 1
while i <= 10:
    print(f"5 × {i} = {5 * i}")
    i += 1
