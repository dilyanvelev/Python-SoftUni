def concatenate(*args, **kwargs):
    new_string = ''.join(args)
    for key,value in kwargs.items():
        if key in new_string:
            new_string = new_string.replace(key,value)
    return new_string

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
