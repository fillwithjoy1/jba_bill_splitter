string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
counter = 0

for i in range(len(string) * len(vowels) + 1):
    if i == 0:
        continue
    if vowels[(i % 5) - 1] == string[(i // 5) - 1]:
        counter += 1
print(counter)
