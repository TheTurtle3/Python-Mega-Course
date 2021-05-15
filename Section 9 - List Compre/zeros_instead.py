def foo(user_list):
    new_list = [x if type(x) == int else 0 for x in user_list]
    
    return new_list