from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError('Name cannot be empty string or white space!')
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        available_foods = {
            'Bread': Bread,
            'Cake': Cake
        }

        if food_type in available_foods:
            if name in [x.name for x in self.food_menu]:
                raise Exception(f'{food_type} {name} is already in the menu!')

            new_food = available_foods[food_type](name, price)
            self.food_menu.append(new_food)
            return f'Added {name} ({food_type}) to the food menu'

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        available_drinks = {
            'Tea': Tea,
            'Water': Water
        }

        if drink_type in available_drinks:
            if name in [x.name for x in self.drinks_menu]:
                raise Exception(f'{drink_type} {name} is already in the menu!')

            new_drink = available_drinks[drink_type](name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f'Added {name} ({drink_type}) to the drink menu'

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table_types = {
            'InsideTable': InsideTable,
            'OutsideTable': OutsideTable
        }

        if table_type in table_types:
            if table_number in [x.table_number for x in self.tables_repository]:
                raise Exception(f'Table {table_number} is already in the bakery!')

            new_table = table_types[table_type](table_number, capacity)
            self.tables_repository.append(new_table)
            return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f'Table {table.table_number} has been reserved for {number_of_people} people'
        return f'No available table for {number_of_people} people'

    def order_food(self, table_number: int, *args):


    def order_drink(self, table_number: int, *args):


    def leave_table(self, table_number):
        table = [x for x in self.tables_repository if x.table_number == table_number][0]
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f'Table: {table_number}\n' \
               f'Bill: {bill:.2f}'

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            if not table.is_reserved:
                result += f'{table.free_table_info()}\n'
        return result

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'


test_bakery = Bakery('Ma Bakery')
print(test_bakery.add_food('Bread', 'Ezekiel', 12))
# print(test_bakery.add_food('Bread', 'Ezekiel', 12))
print(test_bakery.food_menu)
print(test_bakery.add_drink('Water', 'Coke Zero', 220, 'Coca Cola'))
# print(test_bakery.add_drink('Water', 'Coke Zero', 220, 'Coca Cola'))
print(test_bakery.add_table('InsideTable', 12, 5))
print(test_bakery.add_table('InsideTable', 18, 5))
print(test_bakery.add_table('InsideTable', 13, 5))
# print(test_bakery.reserve_table(11))
print(test_bakery.order_food(12, 'Ezekiel', 'Babikiel', 'Grrrer'))
print(test_bakery.order_drink(12, 'Coke Zero', 'Coke Zero', 'Grrrer'))
print(test_bakery.leave_table(12))
print(test_bakery.get_free_tables_info())
print(test_bakery.get_total_income())

