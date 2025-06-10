# Project : Squaring Even Numbers from 1 to 10.

# Using list comprehension to square even numbers
squared_even = [num ** 2 for num in range(1, 11) if num % 2 == 0]

# Print the results with better formatting
print("Squared even numbers from 1 to 10:")
for num, square in zip(range(2, 11, 2), squared_even):
    print(f"{num} squared = {square}")