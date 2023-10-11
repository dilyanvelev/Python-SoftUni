def vowel_filter(function):
    vowels = 'aeiouy'
    def wrapper():
        result = function()
        return [char for char in vowels if char in result]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
