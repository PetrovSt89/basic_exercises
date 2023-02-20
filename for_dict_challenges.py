# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
def diction_name_count(lis):
    repeat = {}
    for key_name in range(len(lis)):
        name = lis[key_name]['first_name']
        if name not in repeat:
            repeat[name] = 1
        else:
            repeat[name] += 1
    return repeat        

for name,count in diction_name_count(students).items():
    print(f'{name}: {count}')    
print()

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
repeat = diction_name_count(students)      
def max_name(diction):
    max_count = 0
    for name,count in diction.items():
        if count > max_count:
            max_count = count
            max_n = name
    return max_n 


print(f'самое частое имя среди учеников: {max_name(repeat)}')    
print()


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for classes in range(len(school_students)):
    print(f'Самое частое имя в классе {classes+1}: {max_name(diction_name_count(school_students[classes]))} ')
print()    

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for classy in range(len(school)):
    clas = school[classy]
    nomer_classa = clas['class']
    boys = []
    girls = []
    student = clas['students']
    for n in student:
        name = n['first_name']
        if is_male[name] == True:
            boys.append(name)
        else:
            girls.append(name) 
    count_boys = len(boys) 
    count_girls = len(girls)       
    print(f'Класс {nomer_classa}: девочки {count_girls}, мальчики {count_boys}')    
print()



   


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
clas_count_boys = 0
clas_count_girls = 0
clas_max_boys = ''
clas_max_girls = ''

for classy in range(len(school)):
    clas = school[classy]
    nomer_classa = clas['class']
    boys = []
    girls = []
    student = clas['students']

    for elem in student:
        name = elem['first_name']

        if is_male[name] == True:
            boys.append(name)
        else:
            girls.append(name) 

    count_boys = len(boys) 
    count_girls = len(girls)     

    if count_boys > clas_count_boys:
        clas_count_boys = count_boys
        clas_max_boys = nomer_classa

    if count_girls > clas_count_girls:
        clas_count_girls = count_girls
        clas_max_girls = nomer_classa    
print(f'Больше всего мальчиков в классе {clas_max_boys}')
print(f'Больше всего девочек в классе {clas_max_girls}')  
print()
