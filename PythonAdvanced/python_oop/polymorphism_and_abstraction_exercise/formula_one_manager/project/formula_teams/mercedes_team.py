from project.formula_teams.formula_team import FormulaTeam
# from python_oop.polymorphism_and_abstraction_exercise.formula_one_manager.project.formula_teams.formula_team import \
#     FormulaTeam


class MercedesTeam(FormulaTeam):

    def __init__(self, budget):
        super().__init__(budget)

    @property
    def sponsors(self):
        return {
            "Petronas": {
                1: 1000000,
                3: 500000
            },
            "TeamViewer": {
                5: 100000,
                7: 50000
            }
        }

    @property
    def expenses_for_one_race(self):
        return 200000
    # def calculate_revenue_after_race(self, race_pos: int):
    #     sponsors = {
    #         "Petronas": {
    #             1: 1000000,
    #             3: 500000
    #         },
    #         "TeamViewer": {
    #             5: 100000,
    #             7: 50000
    #         }
    #     }
    #     earned_money = 0
    #     if race_pos == 1 or race_pos == 3:
    #         money = sponsors["Petronas"][race_pos]
    #         earned_money += money
    #
    #     if race_pos == 5 or race_pos == 7:
    #         money = sponsors["TeamViewer"][race_pos]
    #         earned_money += money
    #     total = earned_money - MercedesTeam.EXPENSES_PER_RACE
    #     self.budget += total
    #     return f"The revenue after thе race is {total}$. Current budget {self.budget}$"
