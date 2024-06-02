word1 = input().strip()
word2 = input().strip()
if len(word1) != len(word2):
    print(-1)
else:
    concatenated_word = word1 + word1
    if word2 in concatenated_word:
        print(1)
    else:
        print(-1)