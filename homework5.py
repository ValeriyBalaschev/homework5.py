# homework5.py Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var = 'Atlas', 5, 255, 100, False
print('immutable_tuple:', immutable_var)
# immutable_var[3] = 225 -  кортеж не изменяемый тип данных,  TypeError: объект 'tuple' не
# поддерживает назначение элементов
mutable_list = ['Atlas', 5, 255, 100, False]
mutable_list[0] = 'New Atlas'
mutable_list[4] = 'Modified'
mutable_list.remove(100)
mutable_list.append('banana')
print('mutable_list:', mutable_list)
