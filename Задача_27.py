# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13

# .lower() - убирает регистр
# len() - выводит длинну списку
# set() - делает из списка множество (в нем нет повторяющихся элементов)
# .split() - убирает элемент по умолчанию пробел

# Первый вариант
# input_text = """She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"""
# print(len(set(input_text.lower().split())))

# Второй вариант
text = ("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells").lower()
# print((text))
# print()
# print(set(text))
# for i in range(len(set(text))):
#     i+=1
#     print(i)

print(len(set(text.split())))