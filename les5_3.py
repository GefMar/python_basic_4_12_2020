from typing import List
from collections import defaultdict
import os



def get_words(file_path: str) -> List[str]:
    with open(file_path, 'r', encoding='UTF-8') as file:
        return file.read().split()


def save_anagrams(file_path: str, data: List[List[str]]):
    with open(file_path, 'w', encoding='UTF-8') as file:
        for itm in data:
            file.write(', '.join(itm) + '\n')
            # print(', '.join(itm), file=file)


def anagrams(words: List[str]) -> List[List[str]]:
    result = defaultdict(list)
    for word in words:
        result[''.join(sorted(word))].append(word)
    return list(result.values())


file_name = 'words.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)
result_file_path = os.path.join(os.path.dirname(__file__), 'anagram_results.txt')

save_anagrams(result_file_path, anagrams(get_words(file_path)))
print(1)
