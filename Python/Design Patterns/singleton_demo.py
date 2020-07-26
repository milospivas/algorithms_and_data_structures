from singleton import SimpleSingleton

a = SimpleSingleton()
b = SimpleSingleton()

print('a:', a)
print('b:', b)

print('id(a) =', id(a))
print('id(b) =', id(b))
print('Are they the same object?', a is b)


print()


from singleton import Singleton

a = Singleton()
b = Singleton()

print('a:', a)
print('b:', b)

print('id(a) =', id(a))
print('id(b) =', id(b))
print('Are they the same object?', a is b)

