immutable_var = ('apple', 'melon', 234, 7.3)
print(immutable_var)
# immutable_var[0] = 'pineapple'  #кортеж неизменяемый тип данных
mutable_list = ['apple', 'melon', 234, 7.3]
mutable_list[0] = 'frog'
mutable_list.pop(2)
mutable_list.append(456)
print(mutable_list)
