# Problem 13: Find sum of even numbers from 1 to 50
# Find and fix the error

 total = 0
for i in range(2, 50, 2):  # start=2, stop=50 (exclusive), step=2
    total += i

print(f"Sum of even numbers: {total}")
