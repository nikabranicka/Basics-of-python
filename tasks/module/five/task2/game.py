import random
import sys

from tasks.module.five.task1.inventory import Item, Inventory, LIGHT_WEIGHT_THRESHOLD, HEAVY_WEIGHT_THRESHOLD, \
    MAX_CAPACITY_THRESHOLD, Food


class Hero:
    player_position_x = 0
    player_position_y: int
    stamina = 100
    normal_stamina = 10
    light_stamina = 20
    heavy_stamina = 50
    my_inventory = Inventory()

    def __init__(self, player_position_y):
        self.player_position_y = player_position_y - 1

    def check_stamina(self):
        """
           Method responsible for controlling stamina level
        """

        total_weight = self.my_inventory.get_weight()
        stamina_used = 10
        if LIGHT_WEIGHT_THRESHOLD <= total_weight < HEAVY_WEIGHT_THRESHOLD:
            print("CAUTION: Your backpack weighs a lot, using " + str(self.light_stamina) + " stamina")
            stamina_used = self.light_stamina
        elif HEAVY_WEIGHT_THRESHOLD <= total_weight < MAX_CAPACITY_THRESHOLD:
            print("CAUTION: Your equipment is very heavy, using " + str(self.heavy_stamina) + " stamina!")
            stamina_used = self.heavy_stamina
        elif total_weight >= MAX_CAPACITY_THRESHOLD:
            print("CAUTION: You are overloaded, need to throw something away...")
            self.my_inventory.remove_item_from_inventory_due_to_overweight(total_weight)
            return False
        if self.stamina - stamina_used >= 0:
            self.stamina -= stamina_used
            print('Used ' + str(stamina_used) + ' stamina')
            return True

        print('Stamina level is ' + str(self.stamina) + ' but you need ' + str(stamina_used) + ' to move!')
        if not (any(isinstance(x, Food) for x in self.my_inventory.inventory)):
            print('No food in inventory, game over!')
            sys.exit('GAME OVER')
        for item in self.my_inventory.inventory:
            if isinstance(item, Food):
                print('Eating ' + item.name + ' for 50 stamina.')
                self.my_inventory.inventory.remove(item)
                self.stamina += 50
                return False


class Board:
    wall_start = '+'
    field_start = '|'
    wall_unit = '---+'
    field_unit = '   |'
    hero_icon = 'H'
    item_icon = 'X'
    board_width = 0
    board_height = 0
    items_positions = set()
    item_count: int
    items: list

    def __init__(self, board_width, board_height, items):
        self.board_width = board_width
        self.board_height = board_height
        self.item_count = random.randint(1, board_width * board_height - 1)
        self.items = items

    def get_random_map_position(self):
        return {(random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1))}

    def create_map_for_hero(self, hero):
        for _ in range(self.item_count):
            random_position = self.get_random_map_position()
            while random_position == {(hero.player_position_x, hero.player_position_y)}:
                random_position = self.get_random_map_position()
            self.items_positions.update(random_position)
        print('Board contains ' + str(len(self.items_positions)) + ' items.')

    def display_board_for(self, hero):
        """
           Method responsible for displaying current state of board
        """

        print('You are the H letter on the board')
        print('X is an random item')
        wall = self.wall_start + self.wall_unit * self.board_width
        print(wall)
        for i in range(self.board_height):
            line = self.field_start + self.field_unit * self.board_width
            for x, y in self.items_positions:
                if i == y:
                    line = line[:(2 + (4 * x))] + self.item_icon + line[(3 + (4 * x)):]
            if i == hero.player_position_y:
                line = line[:(2 + (4 * hero.player_position_x))] \
                       + self.hero_icon + line[(3 + (4 * hero.player_position_x)):]
            print(line)
            print(wall)

    def move_player(self, hero, direction):
        """
           Method responsible for moving player in specified direction
        """

        if direction == 'up':
            if hero.player_position_y == 0:
                print("~~You hit the top wall! Try moving in a different direction~~")
                return
            else:
                hero.player_position_y -= 1
        elif direction == 'down':
            if hero.player_position_y == self.board_height - 1:
                print("~~You hit the bottom wall! Try moving in a different direction~~")
                return
            else:
                hero.player_position_y += 1
        elif direction == 'left':
            if hero.player_position_x == 0:
                print("~~You hit the left wall! Try moving in a different direction~~")
                return
            else:
                hero.player_position_x -= 1
        elif direction == 'right':
            if hero.player_position_x == self.board_width - 1:
                print("~~You hit the right wall! Try moving in a different direction~~")
                return
            else:
                hero.player_position_x += 1
        else:
            print("~~I don't recognize that direction. Try up/down/left/right!~~")
            return
        if hero.check_stamina():
            print("Moved " + direction + "!")
            self.check_item_as(hero)
        else:
            print('Try moving again.')

    def check_item_as(self, hero):
        """
           Method responsible for checking found items
        """

        current_position = hero.player_position_x, hero.player_position_y
        if current_position in self.items_positions:
            item = random.choice(self.items)
            print('Found a >> ' + item.name + "<<!")
            hero.my_inventory.add_to_inventory(item)
            hero.my_inventory.display_inventory()
            self.items_positions.remove(current_position)


class Game:
    initial_map_height_and_hero_position = 3
    initial_map_width = 3
    hero = Hero(initial_map_height_and_hero_position)
    board: Board

    def __init__(self, items):
        self.board = Board(self.initial_map_width, self.initial_map_height_and_hero_position, items)

    def start_game(self):
        self.board.create_map_for_hero(self.hero)
        self.board.display_board_for(game.hero)

    def play_game(self):
        while True:
            print('Stamina level is ' + str(game.hero.stamina))
            game.board.move_player(game.hero, input('Choose a direction to move!\n'))
            game.board.display_board_for(game.hero)


if __name__ == "__main__":
    potential_items = [Item("Hammer", 5, 100), Food('Beef', 2, 10), Food('Herbs', 1, 10), Item("Axe", 5, 50),
                       Item("Sword", 5, 100), Food('Apple', 1, 4), Item("Dragon Head", 10, 1000)]

    game = Game(potential_items)
    game.start_game()
    game.play_game()
