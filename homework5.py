# Создали переменную и присвоили ей кортеж из нескольких элементов разных типов данных.
immutable_var= 41, 'text', 3.23, False
print('Immutable tuple:',immutable_var)

#immutable_var [0] = [99]
# Объяснение:
# Кортежи в Python - это неизменяемые (immutable) структуры данных.
# Это означает, что после их создания, изменить их содержимое нельзя.

# Создали переменную и присвоили ей список из нескольких элементов.
mutable_list = [1, 'cold', 'apple', 4.1]
mutable_list[1] = 222  # Изменяем второй элемент списка
mutable_list [3] = 'fish' # Изменяем четвертый элемент списка
print('Mutable list:',mutable_list) # Вывод списка на экран
