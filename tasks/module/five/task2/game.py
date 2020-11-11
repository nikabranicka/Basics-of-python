import random

from tasks.module.five.task1.Inventory import Item, Inventory, LIGHT_WEIGHT_THRESHOLD, HEAVY_WEIGHT_THRESHOLD, \
    MAX_CAPACITY_THRESHOLD, Food

potential_items = [Item("Hammer", 10, 100), Food('Beef', 2, 10), Food('Herbs', 1, 10), Item("Axe", 5, 50),
                   Item("Sword", 10, 100), Food('Apple', 1, 4), Item("Dragon Head", 12, 1000)]


class Game:
    my_inventory = Inventory()
    my_inventory.display_inventory()


def remove_item_from_inventory(total_weight):
    while total_weight >= MAX_CAPACITY_THRESHOLD:
        removed_item = game.my_inventory.inventory.pop(0)
        print('Removing an item: ' + removed_item.name)
        total_weight = game.my_inventory.get_inventory_weight()


class Board:
    board_width = 3
    board_height = 3
    wall_start = '+'
    field_start = '|'
    wall_unit = '---+'
    field_unit = '   |'
    hero_icon = 'H'
    item_icon = 'X'
    player_position_x = 0
    player_position_y = board_height - 1
    stamina = 100
    normal_stamina = 10
    light_stamina = 20
    heavy_stamina = 50
    item_count = random.randint(1, board_width * board_height - 1)
    items_positions = set()

    def __init__(self):
        for _ in range(self.item_count):
            random_position = {(random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1))}
            while random_position == {(self.player_position_x, self.player_position_y)}:
                random_position = {(random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1))}
            self.items_positions.update(random_position)
        print('Board contains ' + str(len(self.items_positions)) + ' items.')

    def display_board(self):
        wall = self.wall_start + self.wall_unit * self.board_width
        print(wall)
        for i in range(self.board_height):
            line = self.field_start + self.field_unit * self.board_width
            for x, y in self.items_positions:
                if i == y:
                    line = line[:(2 + (4 * x))] + self.item_icon + line[(3 + (4 * x)):]
            if i == self.player_position_y:
                line = line[:(2 + (4 * self.player_position_x))] \
                       + self.hero_icon + line[(3 + (4 * self.player_position_x)):]
            print(line)
            print(wall)

    def move_player(self, direction):
        if direction == 'up':
            if self.player_position_y == 0:
                print("~~You hit the top wall! Try moving in a different direction~~")
                return
            else:
                self.player_position_y -= 1
        elif direction == 'down':
            if self.player_position_y == self.board_height - 1:
                print("~~You hit the bottom wall! Try moving in a different direction~~")
                return
            else:
                self.player_position_y += 1
        elif direction == 'left':
            if self.player_position_x == 0:
                print("~~You hit the left wall! Try moving in a different direction~~")
                return
            else:
                self.player_position_x -= 1
        elif direction == 'right':
            if self.player_position_x == self.board_width - 1:
                print("~~You hit the right wall! Try moving in a different direction~~")
                return
            else:
                self.player_position_x += 1
        else:
            print("~~I don't recognize that direction. Try up/down/left/right!~~")
            return
        if self.check_stamina():
            print("Moved " + direction + "!")
            self.check_item()
        else:
            print('Try moving again.')

    def check_item(self):
        current_position = self.player_position_x, self.player_position_y
        if current_position in self.items_positions:
            item = random.choice(potential_items)  # TODO add randomization
            print('Found a >> ' + item.name + "<<!")
            game.my_inventory.add_to_inventory(item)
            game.my_inventory.display_inventory()
            self.items_positions.remove(current_position)

    def check_stamina(self):
        total_weight = game.my_inventory.get_inventory_weight()
        stamina_used = 10
        if LIGHT_WEIGHT_THRESHOLD <= total_weight < HEAVY_WEIGHT_THRESHOLD:
            print("CAUTION: Your backpack weighs a lot, using " + str(self.light_stamina) + " stamina")
            stamina_used = self.light_stamina
        elif HEAVY_WEIGHT_THRESHOLD <= total_weight < MAX_CAPACITY_THRESHOLD:
            print("CAUTION: Your equipment is very heavy, using " + str(self.heavy_stamina) + " stamina!")
            stamina_used = self.heavy_stamina
        elif total_weight >= MAX_CAPACITY_THRESHOLD:
            print("CAUTION: You are overloaded, need to throw something away...")
            remove_item_from_inventory(total_weight)
            return False
        if self.stamina - stamina_used >= 0:
            self.stamina -= stamina_used
            print('Used ' + str(stamina_used) + ' stamina')
            return True
        else:
            print('Stamina level is ' + str(self.stamina) + ' but you need ' + str(stamina_used) + ' to move!')
            if not (any(isinstance(x, Food) for x in game.my_inventory.inventory)):
                print('No food in inventory, game over!')
                exit('GAME OVER')
            for item in game.my_inventory.inventory:
                if isinstance(item, Food):
                    print('Eating ' + item.name + ' for 50 stamina.')
                    game.my_inventory.inventory.remove(item)
                    self.stamina += 50
                    return False


if __name__ == "__main__":
    game = Game()

    board = Board()
    print('You are the H letter on the board')
    print('X is an random item')
    board.display_board()
    while True:
        print('Stamina level is ' + str(board.stamina))
        board.move_player(input('Choose a direction to move!\n'))
        board.display_board()

    game.my_inventory.display_inventory()
