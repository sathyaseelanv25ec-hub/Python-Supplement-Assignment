# Problem 50: Convert string to uppercase
 text = "python programming"
uppercase = ""

for char in text:
    if 'a' <= char <= 'z':
        uppercase += chr(ord(char) - 32)  # convert to uppercase
    else:
        uppercase += char

print(f"Uppercase: {uppercase}")

