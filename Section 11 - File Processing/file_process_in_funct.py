def foo(ch, filepath):
    with open(filepath) as myfile:
        occurrence = myfile.read().count(ch)
        
    return occurrence