
test_sentance = "write a python program that converts english to piglatin"
test_piglatin = []

for word in test_sentance.split():
    if word[0] in "aeiou":
        print(f"{word[0]}way")
    else:
        print(f"{word[1:]}{word[0]}ay")
