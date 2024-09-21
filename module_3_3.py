def print_params(a = 1, b = 'строка', c = True):
       print(a, b, c)
values_list = [5, 'опять', True]
values_dict = {'a': 'слово', 'b': True, 'c': 3}
print(values_list)
print(values_dict)
values_list_2 = [54.32, 'Строка' ]
print(values_list_2)
print_params ()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params (*values_list )
print_params (**values_dict )
print_params(*values_list_2, 42)






