class vowels:
    ALL_VOWELS = 'AEIUYOaeiuyo'
    def __init__(self, some_string: str):
        self.some_sting = some_string
        self.vowels = [char for char in self.some_sting if char in vowels.ALL_VOWELS]


    def __iter__(self):
        return self


    def __next__(self):

        if not self.vowels:
            raise StopIteration
        return self.vowels.pop(0)





my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

