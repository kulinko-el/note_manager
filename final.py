#Задание 5
note = []
username = input('Введите имя пользователя: ')
title_1 = input('Введите первый заголовок заметки: ')
title_2 = input('Введите второй заголовок заметки: ')
title_3 = input('Введите третий заголовок заметки: ')
content = input('Введите описание: ')
status = input('Введите статус заметки: ')
created_date = input('Введите дату создания в формате дд.мм.гг: ')
issue_date = input('Введите дедлайн в формате дд.мм.гг: ')

note.append(username)
titles = []
titles.append(title_1)
titles.append(title_2)
titles.append(title_3)
note.append(titles)
note.append(content)
note.append(status)
note.append(created_date)
note.append(issue_date)

print('Имя пользователя:', note[0])
print('Заголовок 1:', note[1][0])
print('Заголовок 2:', note[1][1])
print('Заголовок 3:', note[1][2])
print('Описание:', note[2])
print('Статус:', note[3])
print('Дата создания:', note[4][0:5])
print('Дедлайн:', note[5][0:5])