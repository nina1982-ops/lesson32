def custom_write(file_name, strings):
    file_name = 'text.txt'
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i, string in enumerate(strings, 1):
        file.write(string + '\n')
        strings_positions[(i, file.tell())] = string
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
