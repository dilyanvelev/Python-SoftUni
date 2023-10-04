# from python_oop.static_and_class_methods_exercisse.gym.project.customer import Customer
# from python_oop.static_and_class_methods_exercisse.gym.project.equipment import Equipment
# from python_oop.static_and_class_methods_exercisse.gym.project.exercise_plan import ExercisePlan
# from python_oop.static_and_class_methods_exercisse.gym.project.subscription import Subscription
# from python_oop.static_and_class_methods_exercisse.gym.project.trainer import Trainer


from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = next(filter(lambda s: s.id == subscription_id, self.subscriptions))
        customer = next(filter(lambda c: c.id == subscription_id, self.customers))
        trainer = next(filter(lambda t: t.id == subscription_id, self.trainers))
        equipment = next(filter(lambda eq: eq.id == subscription_id, self.equipment))
        plan = next(filter(lambda p: p.id == subscription_id, self.plans))

        return str(subscription) + "\n" + str(customer) + "\n" + str(trainer) + "\n" + \
            str(equipment) + "\n" + str(plan)




# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
#
# gym = Gym()
#
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
#
# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))
