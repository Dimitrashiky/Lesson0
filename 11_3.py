from inspect import getmodule

def introspecation_info(obj):
    return {
        "type": type(obj). __name__,
        "attributes": obj. __dict__,
        "methods": dir(obj),
        "module": getmodule(obj). __name__
    }
class Myclass:
    pass

obj = Myclass

number_info = introspecation_info(obj)
print(number_info)