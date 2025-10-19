import mymodule

print(mymodule.say_hello("World"))

from mymodule import say_hello

print(say_hello("World"))

from mymodule import say_hello as greeting

print(greeting("World"))

from mymodule import say_hello as greeting

print(dir())
print(greeting("World"))