from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wapprer(*args, **kwargs):
        print(f"Here are the args: {(args)}") 
        print(f"Here are the kwargs: {kwargs}") 
        return fn(*args, **kwargs)
    return wapprer

@show_args
def teste(*args, **kwargs):
    pass

teste(1,2,3,a="hi",b="bye")





