# Problem 16: Find the second largest number in a list
# Find and fix the error

 numbers = [45, 89, 12, 78, 34]

# Remove duplicates and sort
unique_numbers = sorted(set(numbers))

# Get second largest
if len(unique_numbers) >= 2:
    second_largest = unique_numbers[-2]
    print(f"Second largest: {second_largest}")
else:
    print("Not enough distinct numbers to find second largest")
