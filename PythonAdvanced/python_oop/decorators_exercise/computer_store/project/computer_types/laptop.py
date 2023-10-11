from project.computer_types.computer import Computer


class Laptop(Computer):
    COMP_PROCESSOR = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200
    }
    COMP_RAM = {
        2: 100,
        4: 200,
        8: 300,
        16: 400,
        32: 500,
        64: 600

    }

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in Laptop.COMP_PROCESSOR:
            raise ValueError(
                f"{self.processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if ram not in Laptop.COMP_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        self.processor = processor
        self.price += Laptop.COMP_PROCESSOR[processor]
        self.ram = ram
        self.price += Laptop.COMP_RAM[ram]
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
