from project.formula_teams.formula_team import FormulaTeam
# from python_oop.polymorphism_and_abstraction_exercise.formula_one_manager.project.formula_teams.formula_team import \
#     FormulaTeam


class RedBullTeam(FormulaTeam):

    def __init__(self, budget):
        super().__init__(budget)

    @property
    def sponsors(self):
        return {
            "Oracle": {
                1: 1500000,
                2: 800000
            },
            "Honda": {
                8: 20000,
                10: 10000
            }
        }

    @property
    def expenses_for_one_race(self):
        return 250000
        # def calculate_revenue_after_race(self, race_pos: int):
    #     sponsors = {
    #         "Oracle": {
    #             1: 1500000,
    #             2: 800000
    #         },
    #         "Honda": {
    #             8: 20000,
    #             10: 10000
    #         }
    #     }
    #     earned_money = 0
    #     if race_pos == 1 or race_pos == 2:
    #         money = sponsors["Oracle"][race_pos]
    #         earned_money += money
    #
    #     if race_pos == 8 or race_pos == 10:
    #         money = sponsors["Honda"][race_pos]
    #         earned_money += money
    #     total = earned_money - RedBullTeam.EXPENSES_PER_RACE
    #     self.budget += total
    #     return f"The revenue after thе race is {total}$. Current budget {self.budget}$"

# red_bull_team = RedBullTeam(1000000)
# print(red_bull_team.calculate_revenue_after_race(1))
