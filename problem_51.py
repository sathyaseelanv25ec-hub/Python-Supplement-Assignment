# Problem 51: Reverse words in a sentence
 def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])  # reverse each word
    return " ".join(reversed_words)

text = "Hello World"
print(f"Reversed words: {reverse_words(text)}")

