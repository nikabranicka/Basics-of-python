import pprint

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

my_inventory = {'gold coin': 42, 'rope': 1}

dragon_loot = ['gold coin', 'chewed gum', 'dagger', 'gold coin', 'gold coin', 'ruby', 'rubbish', 'chewed gum',
               'used tissue']

trash = ['rubbish', 'chewed gum', 'used tissue']


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0

    for item_name, item_count in inventory.items():
        print(f"{str(item_count)} {item_name} ")
        item_total += item_count

    print("*****************************************")
    print(f"Total number of items: {str(item_total)}")

    if 60 <= item_total <= 69:
        print("CAUTION: Your backpack weighs a lot, your stamina runs out quicker!")
    elif 70 <= item_total <= 79:
        print("CAUTION: Your equipment is very heavy, you're moving slower than usual!")
    elif item_total >= 80:
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
    print(pprint.pprint(skipped_items))
    return inventory


my_inventory = add_to_inventory(my_inventory, dragon_loot)
display_inventory(my_inventory)