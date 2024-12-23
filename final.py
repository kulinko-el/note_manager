#Задание 5
note_data = []
username = input('Введите имя пользователя ➣ ')
title_1 = input('Введите первый заголовок заметки ➣ ')
title_2 = input('Введите второй заголовок заметки ➣ ')
title_3 = input('Введите третий заголовок заметки ➣ ')
content = input('Введите описание ➣ ')
status = input('Введите статус заметки ➣ ')
created_date = input('Введите дату создания в формате дд.мм.гг ➣ ')
issue_date = input('Введите дедлайн в формате дд.мм.гг ➣ ')

note_data.append(username)
titles = []
titles.append(title_1)
titles.append(title_2)
titles.append(title_3)
note_data.append(titles)
note_data.append(content)
note_data.append(status)
note_data.append(created_date)
note_data.append(issue_date)

note = {
    'Имя пользователя' : note_data[0],
    'Заголовок 1' : note_data[1][0],
    'Заголовок 2' : note_data[1][1],
    'Заголовок 3' : note_data[1][0],
    'Описание заметки' : note_data[2],
    'Статус заметки' : note_data[3],
    'Дата создания' : note_data[4][0:5],
    'Дедлайн' : note_data[5][0:5]
}

print('👤 Имя пользователя:', note['Имя пользователя'])
print('📎 Заголовок 1:', note['Заголовок 1'])
print('📎 Заголовок 2:', note['Заголовок 2'])
print('📎 Заголовок 3:', note['Заголовок 3'])
print('✏️ Описание заметки:', note['Описание заметки'])
print('🔍 Статус заметки:', note['Статус заметки'])
print('📆 Дата создания:', note['Дата создания'])
print('💣 Дедлайн:', note['Дедлайн'])
