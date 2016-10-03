from inspect import signature

def type_check(func):
    def wrap(*args, **kwargs):
        for key, param in enumerate(signature(func).parameters.values()):
            import pdb; pdb.set_trace() 
            if not isinstance(args[key], param.annotation):
                raise TypeError('Expected %s type and %s received ' % (type(args), param.annotation))

        return func(*args, **kwargs)

    return wrap

@type_check
def mul(x: int, y: int):
    return x * y 

print(mul(20, 10))
