import random

list_of_words = [
    'banana',
    'dog',
    'ball',
    'flash'
]

chosen_word = random.choice(list_of_words)
print (chosen_word)
hidden_list =['' for i in chosen_word]
chosen_list = []
hidden_word = ''
print (hidden_list)
for i in chosen_word:
    print (i)
    chosen_list = chosen_list + [i]
for i in range(len(chosen_list)):
    hidden_list[i] = '|_|'
print(chosen_list)
print(hidden_list)
print('----------')
hidden_word = hidden_word.join(hidden_list)
print(hidden_word)