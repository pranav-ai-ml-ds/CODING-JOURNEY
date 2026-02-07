# PRINT - just displays
def print_double(x):
    print(x * 2)

# RETURN - gives back a value you can use
def get_double(x):
    return x * 2

# Compare:
print_double(5)  # Prints: 10
result = print_double(5)  # Prints 10, but result is None
print(result)  # None

value = get_double(5)  # Doesn't print anything
print(value)  # 10
total = get_double(5) + get_double(3)  # 10 + 6 = 16