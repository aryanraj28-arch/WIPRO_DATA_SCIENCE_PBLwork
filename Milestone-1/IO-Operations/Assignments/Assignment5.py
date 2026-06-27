**Assignment5**
1)file = open("sample.txt", "r")

content = file.read()
print(content)

file.close()

2)
n = int(input("Enter the number of lines to read: "))

file = open("sample.txt", "r")

for i in range(n):
    line = file.readline()

    if line == "":
        break

    print(line, end="")

file.close()

3)
text = input("Enter text to append: ")

file = open("sample.txt", "a")

file.write(text + "\n")

file.close()

print("Data appended successfully.")

4)

file = open("sample.txt", "r")

lines = file.readlines()

file.close()

line_list = []

for line in lines:
    line_list.append(line.strip())

print(line_list)

5)
file = open("sample.txt", "r")

content = file.read()

file.close()

words = content.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

6)
word = input("Enter the word to search: ")

file = open("sample.txt", "r")

content = file.read()

file.close()

words = content.split()

count = 0

for w in words:
    if w == word:
        count += 1

print("Frequency of", word, "is", count)
