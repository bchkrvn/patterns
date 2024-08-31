from factory.factory_model import ValidatorFactory

str_obj = 'some text'
int_obj = 1234
list_obj = ['1', 2]
dict_obj = {'1': 1}

data = {
    'string': str_obj,
    'integer': int_obj,
    'list': list_obj,
    'dict': dict_obj
}

for type_, obj in data.items():
    validator = ValidatorFactory.get_validator(type_=type_)
    validator.validate(obj)


validator = ValidatorFactory.get_validator(type_='string')
obj = 1
try:
    validator.validate(obj)
except TypeError:
    print(f'Объект {obj} не имеет тип {validator.type_}')