data = ['hel', 'low', 'frog', 'hello', 'lohel', 'hlelo', 'leh', ]

result = {}

for word in data:
    sort_word = ''.join(sorted(word))
    if result.get(sort_word):
        result[sort_word].append(word)
    else:
        result[sort_word] = [word]

print(list(result.values()))

# result = [
#     ['hel', 'leh'],
#     ['low'],
#     ['frog']
# ]

