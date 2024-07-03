def print_params (a=1, b='str',c=True):
    print(a,b,c)

print_params (b=25)
print_params(c=[1,2,3])

value_list=[1,3,'string']
value_dict={'a':6, 'b':73, 'c':True}
print_params(*value_list)
print_params (**value_dict)

value_list_2=[54.32,'Строка']
print_params(*value_list_2,42)