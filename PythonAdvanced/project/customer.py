class Customer:
    id = 1

    def __init__(self, name: str, address: str, emails: str):
        self.name = name
        self.address = address
        self.emails = emails
        self.id = Customer.get_next_id()

        Customer.id += 1

    @classmethod
    def get_next_id(cls):
        return cls.id


