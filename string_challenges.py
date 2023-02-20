# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print()


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len(word))
print()


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels ='аоуыэеёиюя'
vowels_list = []
for letter in word.lower():
    if letter in vowels:
        vowels_list.append(letter)
print(len(vowels_list))
print()


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split()
print(len(sentence))
print()

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence = sentence.split()
for word in sentence:
    print(word)
print()    


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split()
sum = 0
for word in sentence:
    sum += len(word)
average = sum//len(sentence)
print(average)
print()
