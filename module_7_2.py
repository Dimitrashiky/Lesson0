def custom_write(file_name, strings):
    name_file = open(file_name, "a", encoding = "utf-8")
    strings_positions = {}
    string_num = 1
    for string in strings:
        strings_positions[(string_num, name_file.tell())] = string
        name_file.write(string + "\n")
        string_num += 1
    name_file.close()
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