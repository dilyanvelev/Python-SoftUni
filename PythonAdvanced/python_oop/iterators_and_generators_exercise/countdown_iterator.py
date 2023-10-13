class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.counter = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == -1:
            raise StopIteration
        result = self.counter
        self.counter -= 1

        return result


iterator = countdown_iterator(10)
for item in iterator:


    print(item, end=" ")
