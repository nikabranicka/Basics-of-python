from collections import defaultdict

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

my_inventory = {'gold coin': 42, 'rope': 1}

dragon_loot = ['gold coin', 'chewed gum', 'dagger', 'gold coin', 'gold coin', 'ruby', 'rubbish', 'chewed gum',
               'used tissue']

trash = ['rubbish', 'chewed gum', 'used tissue']

LIGHT_WEIGHT_THRESHOLD = 60
HEAVY_WEIGHT_THRESHOLD = 70
MAX_CAPACITY_THRESHOLD = 80


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0

    for item_name, item_count in inventory.items():
        print(f"{item_count} {item_name} ")
        item_total += item_count

    print(f"Total number of items: {str(item_total)}")

    if LIGHT_WEIGHT_THRESHOLD <= item_total < HEAVY_WEIGHT_THRESHOLD:
        print("CAUTION: Your backpack weighs a lot, your stamina runs out quicker!")
    elif HEAVY_WEIGHT_THRESHOLD <= item_total < MAX_CAPACITY_THRESHOLD:
        print("CAUTION: Your equipment is very heavy, you're moving slower than usual!")
    elif item_total >= MAX_CAPACITY_THRESHOLD:
        print("CAUTION: You are overloaded, can't move!")


display_inventory(stuff)


def add_to_inventory(inventory, new_items):
    skipped_items = {}
    added_items_count = 0

    for item in new_items:
        if item in trash:
            if item in skipped_items:
                skipped_items[item] += 1
            else:
                skipped_items[item] = 1
        else:
            if item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1
            added_items_count += 1

    print(f"Total number of added items: {str(added_items_count)}")

    print("Skipped Trash:")
    for item_name, item_count in skipped_items.items():
        print(f"{str(item_count)} {item_name}")

    return inventory


my_inventory = add_to_inventory(my_inventory, dragon_loot)
display_inventory(my_inventory)
