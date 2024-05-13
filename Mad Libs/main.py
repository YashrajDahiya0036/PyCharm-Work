with open("story_aria.txt", "r") as f:
    story = f.read()

start_char = "<"
end_char = ">"
words = set()
start_of_word = -1

for i, char in enumerate(story):
    if char == start_char:
        start_of_word = i
    if char == end_char and start_of_word != -1:
        word = story[start_of_word:i+1]
    # print(i)
        words.add(word)
print(words)
dict1 = {}
for i in words:
    new_word = input(f"Enter the word to replace {i}.")
    dict1[i] = new_word

for i in words:
    story = story.replace(i, dict1[i])

print(story)
