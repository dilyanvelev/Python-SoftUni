class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


# int_list = IntegerList(1, 2, 3)
# int_list.get_biggest()
# int_list.insert(0, 0)

from unittest import TestCase, main


class IntegerListTests(TestCase):
    def setUp(self):
        self.int_list = IntegerList(1, 2, 3, '2', True)

    def test_correct_initialization(self):
        self.assertEqual([1, 2, 3], self.int_list._IntegerList__data)

    def test_get_data_function_return_data(self):
        self.int_list.get_data()
        self.assertEqual([1, 2, 3], self.int_list._IntegerList__data)

    def test_add_element_if_el_is_int_raise_valueError(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.add('1')
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_correct_adding_element_to_data(self):
        self.int_list.add(4)
        self.assertEqual([1, 2, 3, 4], self.int_list._IntegerList__data)

    def test_remove_element_from_data_raise_indexError(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.remove_index(4)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_delete_element_by_index(self):
        self.int_list.remove_index(1)
        self.assertEqual([1, 3], self.int_list._IntegerList__data)

    def test_return_removed_element_if_not_raised_error(self):
        self.assertEqual(2, self.int_list.remove_index(1))

    def test_accessing_failed_element_from_data_raise_indexError(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.get(3)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_return_element_by_index_if_index_correct(self):
        self.assertEqual(1, self.int_list.get(0))

    def test_insert_correct_type_element_at_incorrect_index_raise_indexError(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.insert(3, 4)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_wrong_type_a_correct_index_raise_indexError(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.insert(2, '5')
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_correct_type_at_correct_index(self):
        self.int_list.insert(0, 0)
        self.assertEqual([0, 1, 2, 3], self.int_list.get_data())

    def test_if_get_biggest_method_return_correct_number(self):
        self.assertEqual(3, self.int_list.get_biggest())

    def test_if_get_index_return_correct_element_index(self):
        self.assertEqual(1, self.int_list.get_index(2))


if __name__ == '__main__':
    main()
