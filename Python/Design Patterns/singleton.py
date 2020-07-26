''' Module demonstrating Singleton design pattern:
        1) a simple way, hiding the constructor
        2) via a metaclass

    Author: Miloš, Pivaš
'''

### 1) Hiding the constructor: ################################################

class _SimpleSingleton:
    ''' A simple singleton class.
    '''

    def __str__(self):
        return 'A SimpleSingleton object.'


_instance = None

def SimpleSingleton():
    global _instance
    if _instance is None:
        _instance = _SimpleSingleton()

    return _instance


### 2) From metaclass: ########################################################

class SingletonMeta(type):
    ''' A singleton metaclass.
    '''

    _instances = {}

    def __call__(cls, *args, **kwargs):
        ''' Possible changes to the value of the '__init__' argument
            do not affect the returned instance.
        '''

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    ''' A singleton class.
    '''

    def some_business_logic(self):
        ''' Define some business logic,
            which can be executed on its instance.
        '''
        # ...

    def __str__(self):
        return 'A Singleton object.'