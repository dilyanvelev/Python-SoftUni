class Zoo:
    __animals = 0

    def __init__(self, zoo_name=""):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):

        if species == "mammal":
            return f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"

        elif species == "fish":
            return f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}"

        elif species == "bird":
            return f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {self.__animals}"


name_input = input()
number = int(input())
zoo = Zoo(name_input)

for _ in range(number):
    info = input().split()

    animal_species = info[0]
    animal_name = info[1]

    zoo.add_animal(animal_species, animal_name)

species_list_info = input()
print(zoo.get_info(species_list_info))
