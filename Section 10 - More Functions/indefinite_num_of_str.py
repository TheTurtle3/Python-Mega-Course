def foo(*args):
    new_args = [x.upper() for x in args]
    new_args.sort()
    
    return new_args