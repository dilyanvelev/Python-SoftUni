class reverse_iter:
    def __init__(self, some_list: list):
        self.some_list = some_list

    def __iter__(self):
        return self

    def __next__(self):
        if not self.some_list:
            raise StopIteration

        last_el = self.some_list.pop()
        return last_el

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

