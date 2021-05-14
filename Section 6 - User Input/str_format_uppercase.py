def foo(name):
    name = name[0].upper() + name[1:]
    greetings = "Hi %s" % name
    
    return greetings