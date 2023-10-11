class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('Kiro', 1000, 100)

    def test_initializing(self):
        self.assertEqual('Kiro', self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_increment_energy_rest_method(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_working_with_negative_or_zero_exception_raised(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.worker.work()

    def test_correct_salary_increase(self):
        self.worker.work()
        self.assertEqual(1000, self.worker.money)

    def test_decrease_energy(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_correct_string_return(self):
        self.worker.get_info()
        self.assertEqual('Kiro has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()
