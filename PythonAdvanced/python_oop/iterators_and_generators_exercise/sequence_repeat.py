class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.number:
            raise StopIteration
        if self.index == len(self.sequence):
            self.index = 0
        idx = self.index
        self.index += 1
        self.counter += 1
        return self.sequence[idx]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

