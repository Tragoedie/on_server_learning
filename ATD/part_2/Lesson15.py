class Warrior:
    def __init__(self):
        self._creation_time = 100
        self._resources_cost = {'food': 100, 'wood': 75}
        self._unit_name = 'Warrior'

    def _spend_resources(self):
        for resource, cost_val in self._resources_cost.items():
            print_str = '{0} spent: {1}'.format(resource, cost_val)
            print(print_str)
        print('Time spent: ', self._creation_time)

    def _print_message(self):
        print(self._unit_name, " successfully created!")

    def create_unit(self):
        self._spend_resources()
        self._print_message()


class Archer(Warrior):
    def __init__(self):
        self._creation_time = 150
        self._resources_cost = {'food': 75, 'wood': 125, 'gold': 25}
        self._unit_name = 'Archer'


class Barracs:
    def __init__(self):
        self.__created_unit = None

    def set_unit_type(self, unit):
        self.__created_unit = unit

    def create_new_unit(self):
        self.__created_unit.create_unit()


barracs = Barracs()
warrior = Warrior()
archer = Archer()
barracs.set_unit_type(warrior)
barracs.create_new_unit()
# food spent: 100
# wood spent: 75
# Time spent:  100
# Warrior successfully created!
barracs.set_unit_type(archer)
barracs.create_new_unit()
# food spent: 75
# wood spent: 125
# gold spent: 25
# Time spent:  150
# Archer successfully created!
