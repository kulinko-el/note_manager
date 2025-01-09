#Задание 4
username = input('Введите имя пользователя: ')
title_1 = input('Введите первый заголовок заметки: ')
title_2 = input('Введите второй заголовок заметки: ')
title_3 = input('Введите третий заголовок заметки: ')
content = input('Введите описание: ')
status = input('Введите статус заметки: ')
created_date = input('Введите дату создания в формате дд.мм.гг')
issue_date = input('Введите дедлайн в формате дд.мм.гг')

titles = []
titles.append(title_1)
titles.append(title_2)
titles.append(title_3)

print('Имя пользователя:', username)
print('Первый заголовок заметки:', titles[0])
print('Второй заголовок заметки:', titles[1])
print('Третий заголовок заметки:', titles[2])
print('Описание заметки:', content)
print('Статус заметки:', status)
print('Дата создания заметки:', created_date[:5])
print('Дедлайн:', issue_date[:5])
