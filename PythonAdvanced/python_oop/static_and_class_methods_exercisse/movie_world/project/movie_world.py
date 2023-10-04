from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []  # capacity=customer_capacity()
        self.dvds = []  # capacity=dvd_capacity()

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        customer_capacity = MovieWorld.customer_capacity()
        # TODO:check =
        if len(self.customers) < customer_capacity:
            self.customers.append(customer)  # name, age, id

    def add_dvd(self, dvd: DVD):
        dvd_capacity = MovieWorld.dvd_capacity()
        if len(self.dvds) < dvd_capacity:
            self.dvds.append(dvd)  # name, id, creation_year, creation_month, age_restriction

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = next(filter(lambda c: c.id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = next(filter(lambda c: c.id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        customer_strings = [str(customer) for customer in self.customers]
        dvd_strings = [str(dvd) for dvd in self.dvds]

        return '\n'.join(customer_strings) + "\n" + '\n'.join(dvd_strings)

