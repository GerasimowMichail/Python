# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text_input = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'
print(f'Исходный текст: {text_input} ')
def del_words_abw(text_input):
    text_input = list(filter(lambda x: 'абв' not in x, text_input.split()))
    return " ".join(text_input)

print()
text_output = del_words_abw(text_input)
print(f'Обработанный текст:      {text_output}')