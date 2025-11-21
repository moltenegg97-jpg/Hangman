import json
from pathlib import Path

path_to_original = Path('words.json')

with open(path_to_original) as file:
        list_of_words= json.load(file)

for word in list_of_words:
    for i in range (len(word)):
          if word[i] == ' ':
            print(word, list_of_words.index(word))

for i in range(len(list_of_words)):
    word = list_of_words[i]
    if ' ' in word:
        splited_word_list = word.split(' ')
        list_of_words[i] = splited_word_list[0]

for word in list_of_words[:]:  # итерируемся по копии
    if '-' in word:
        list_of_words.remove(word)


# Преобразуем в JSON строку
json_string = json.dumps(list_of_words, ensure_ascii=False, indent=4)

with open('new_file.json', 'w', encoding='utf-8') as file:
    file.write(json_string)

