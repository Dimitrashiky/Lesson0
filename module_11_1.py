import inspect


class MyClass:

    def __init__(self):
        self.parameter = 1000
        self.fname = 'file.txt'

    def set_param(self, value):
        self.parameter = value

    def __add__(self, other):
        self.parameter += other.parameter
        return self

    def __str__(self):
        return str(self.parameter)


def show_all(*args):
    for j, _ in enumerate(*args):
        print(j, _)


def introspection_info(obj):
    info = {}

    info['name'] = getattr(obj, '__name__', 'без имени')
    info['type'] = type(obj)

    attributes = []
    methods = []

    for _ in dir(obj):
        # print(_, type(getattr(obj, _)))
        type_ = str(type(getattr(obj, _)))
        if 'method' in type_ or 'function' in type_ or 'wrapper' in type_:
            methods.append(_)
        else:
            attributes.append(_)

    info['attributes'] = attributes
    info['methods'] = methods
    info['callable'] = callable(obj)
    info['module'] = inspect.getmodule(obj)

    return info


def main():
    a = MyClass()
    # b = MyClass()
    a.set_param(2000)
    # c = a + b
    # show_all([a, b, c])

    print(introspection_info(42))
    print(introspection_info(MyClass))
    print(introspection_info(show_all))


if __name__ == '__main__':
    main()
