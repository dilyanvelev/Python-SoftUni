class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.counter = 0
        self.dict_items = [item for item in self.dictionary.items()]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == len(self.dict_items):
            raise StopIteration
        index = self.counter
        self.counter += 1

        return self.dict_items[index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

