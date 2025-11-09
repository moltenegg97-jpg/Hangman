import random

list_of_words = [
    'banana',
    'dog',
    'ball',
    'flash',
    'arrow',
    'sword',
    'monkey',
    'bishop',
    'egg',
    'silk'
]
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

def guess_letter():
    print('enter letter')
    guessted_letter = input().lower()
    if guessted_letter in used_letters:
        print(f'эта буква уже была, попробуйте снова')
        guess_letter()
        
    if len(guessted_letter) > 1:
        print(f'введите 1 букву')
        guess_letter()
    if any(char.isnumeric() for char in guessted_letter):
        print ('введена цифра, введите букву')
        guess_letter()
    return guessted_letter

while turn < 10 and '|_|' in hidden_list:
    print(f'turn: {turn}')
    guessted_letter = guess_letter()
    for i in range(len(chosen_word)):
        if guessted_letter == chosen_list[i]:
            hidden_list[i] = chosen_list[i]
    if guessted_letter not in chosen_word:
        print('этой буквы нет в слове')
    used_letters = used_letters + [f'{guessted_letter}']
    hidden_word = ''        
    hidden_word = hidden_word.join(hidden_list)
    print(f'used_letters: {used_letters}')
    print(hidden_word)

    turn += 1
    if '|_|' not in hidden_list:
        print('Победа!')
        break
    if turn == 10:
        print('Поражение')

print('игра окончена')