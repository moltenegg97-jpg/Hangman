import random
from pathlib import Path
import json
import my_drawing


new_drawing = my_drawing.DrawingHangman()
file_path = Path('words.json')

if file_path.exists():
    print("Файл найден! Открываю...")
    with open(file_path) as file:
        list_of_words= json.load(file)
        # print (list_of_words)
        # print (type(list_of_words))
        # for line in file:
        #      list_of_words.append(line.strip())
        #print(contents) # ... ваш код для работы с файлом
else:
    print("Файл не найден. Проверьте название и путь.")

turn = 0 #номер хода
used_letters = [] #список использованных букв
chosen_word = random.choice(list_of_words) #выбор случайного слова из списка
print (chosen_word)
hidden_list =['' for i in chosen_word] #создание пустого списка с длиной слова
chosen_list = [] #список из букв выбранного слова
hidden_word = ''#строка отвечающая за слово сл скрытыми буквами
print (hidden_list)

for i in chosen_word: #перевод из строки в список
    chosen_list = chosen_list + [i]
for i in range(len(chosen_list)): #создание скрытого списка
    hidden_list[i] = '|_|'
print(chosen_list)
print(hidden_list)
print('----------')
hidden_word = hidden_word.join(hidden_list) #перевод скрытого списка в строку
print(hidden_word)

def try_to_guess():
    print('enter letter')
    guessted_letter = input().upper()
    if guessted_letter in used_letters:
        print(f'эта буква уже была, попробуйте снова')
        return   
    if len(guessted_letter) == 0:
        print(f'введите букву')
        return
    if len(guessted_letter) > 1:
        print(f'введите 1 букву')
        return
    if any(char.isnumeric() for char in guessted_letter):
        print ('введена цифра, введите букву')
        return
        
    return guessted_letter

while turn < 6 and '|_|' in hidden_list:
    if turn == 0:
        new_drawing.partial_drawing(turn)
    print(f'turn: {turn}')
    guessted_letter = try_to_guess()
    while guessted_letter == None:
        guessted_letter = try_to_guess()
    for i in range(len(chosen_word)):
        if guessted_letter == chosen_list[i]:
            hidden_list[i] = chosen_list[i]
    if guessted_letter not in chosen_word:
        print('этой буквы нет в слове')
        turn += 1
    used_letters = used_letters + [f'{guessted_letter}']
    hidden_word = ''        
    hidden_word = hidden_word.join(hidden_list)
    print(f'used_letters: {used_letters}')
    print(hidden_word)
    
    if turn != 0:
        new_drawing.partial_drawing(turn)
    if '|_|' not in hidden_list:
        print('Победа!')
        break
    if turn == 6:
        print('Поражение')

my_drawing.turtle.mainloop()

print('игра окончена')