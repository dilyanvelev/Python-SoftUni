class Inventory:
    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.default_capacity = __capacity
        self.items = []

    def add_item(self, item: str):
        if not self.__capacity:
            return "not enough room in the inventory"
        self.items.append(item)
        self.__capacity -= 1

    def get_capacity(self):
        return self.default_capacity

    def __repr__(self):

        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
