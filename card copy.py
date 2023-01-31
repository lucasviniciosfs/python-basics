from functools import wraps

def ensure_authorized(fn):
    wraps(fn)
    def wrap(*args, **kwargs):
        if kwargs.get('role') == "admin":
            return fn(*args, **kwargs)
        else:
            return print("Unauthorized")
        
    return wrap


@ensure_authorized
def show_secrets(*args, **kwargs):
    return print("Shh! Don't tell anybody!")

show_secrets(role="admin")
show_secrets(role="nobody")
