from collections import namedtuple

# Створення іменованого кортежу
Point = namedtuple('Point', ['x', 'y'])

# Створення екземпляра Point
p = Point(11, y=22)

print(p.x)  # 11
print(p.y)  # 22