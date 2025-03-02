def count_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."

filename = "quote.txt"
count = count_words(filename)
print(f"How many words in this file: {filename}: {count}")