def foo(user_list):
    new_list = [x for x in user_list if type(x) == int]
    
    return new_list