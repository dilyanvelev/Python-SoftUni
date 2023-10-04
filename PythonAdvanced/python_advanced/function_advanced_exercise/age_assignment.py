def age_assignment(*args, **kwargs):
    dictionary = {}
    for name in args:
        for key, value in kwargs.items():
            if name[0] == key:
                if name not in dictionary:
                    dictionary[name] = value
    new_dictionary = sorted(dictionary.items())
    result = ''
    for name, age in new_dictionary:
        result += f"{name} is {age} years old." + "\n"
    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
