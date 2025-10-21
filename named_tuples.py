import collections

# Створення іменованого кортежу Person
Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# Створення екземпляра Person
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# Створення іменованого кортежу Cat
Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner']) 
        
cat = Cat('Simon', 4, 'Krabat') 

print(f'This is {cat.nickname}, a {cat.age}-year-old cat. His owner is {cat.owner}')