from collections import defaultdict
from dataclasses import dataclass

LIGHT_WEIGHT_THRESHOLD = 6
HEAVY_WEIGHT_THRESHOLD = 10
MAX_CAPACITY_THRESHOLD = 14

items_to_skip = ['rubbish', 'chewed gum', 'used tissue']


@dataclass
class Item:
    name: str
    weight: int
    price: int


@dataclass
class Food:
    name: str
    weight: int
    price: int


class Inventory:

    def __init__(self):
        self.inventory = []

    def get_inventory_weight(self):
        total_weight = 0
        for item in self.inventory:
            total_weight += item.weight
        return total_weight

    def display_inventory(self):
        print("Inventory:")
        total_weight = 0
        for item in self.inventory:
            print(f"{item.name} weight {item.weight} price {item.price}")
            total_weight += item.weight
        print(f"Total weight of items: {str(total_weight)}")

        if LIGHT_WEIGHT_THRESHOLD <= total_weight < HEAVY_WEIGHT_THRESHOLD:
            print("CAUTION: Your backpack weighs a lot, your stamina runs out quicker!")
        elif HEAVY_WEIGHT_THRESHOLD <= total_weight < MAX_CAPACITY_THRESHOLD:
            print("CAUTION: Your equipment is very heavy, you're moving slower than usual!")
        elif total_weight >= MAX_CAPACITY_THRESHOLD:
            print("CAUTION: You are overloaded, can't move!")

    def add_to_inventory(self, new_item: Item):
        skipped_items = defaultdict(int)

        added_items_count = 0

        if new_item.name in items_to_skip:
            skipped_items[new_item] += 1
        else:
            self.inventory.append(new_item)
            added_items_count += 1

        return self.inventory


if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_to_inventory(Item('gold coin', 1, 1))
    inventory.add_to_inventory(Item('gold coin', 1, 1))
    inventory.add_to_inventory(Item('sword', 50, 30))
    inventory.display_inventory()
