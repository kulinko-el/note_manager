#Задание 3
username = input('Введите имя пользователя: ')
title = input('Введите заголовок заметки: ')
content = input('Введите описание: ')
status = input('Введите статус заметки: ')
created_date = input('Введите дату создания в формате дд.мм.гг')
issue_date = input('Введите дедлайн в формате дд.мм.гг')

print('Имя пользователя:', username)
print('Заголовок заметки:', title)
print('Описание заметки:', content)
print('Статус заметки:', status)
print('Дата создания заметки:', created_date[0:5])
print('Дедлайн:', issue_date[0:5])
