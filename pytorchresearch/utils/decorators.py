
def unfinished_function(func):
    def result(*args, **kwargs):
        print('Function {} is unfinished'.format(func.__name__) +
              'and not enough tested. '
              'Be careful with it.')
        func(*args, **kwargs)
    return result


def unfinished_class(cls):
    def new(cls, *args, **kwargs):
        result = object.__new__(cls)
        cls.__init__(result, *args, **kwargs)
        print('Class {} is unfinished'.format(cls.__name__) +
              'and not enough tested. '
              'Be careful with it.')
        return result
    cls.__new__ = new
    return cls


if __name__ == "__main__":
    @unfinished_class
    class X:
        def __init__(self, x):
            self.x = x

    print(X(10).x)
