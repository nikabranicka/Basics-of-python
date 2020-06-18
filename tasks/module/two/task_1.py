stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0

    for item_name, item_count in inventory.items():
        print(f"Item: {item_name}  -> Amount: {str(item_count)}")
        item_total += item_count

    print("*****************************************")
    print(f"Total number of items: {str(item_total)}")

    if 60 < item_total <= 69:
        print("CAUTION: Your backpack weighs a lot, your stamina runs out quicker!")
    elif 70 < item_total <= 79:
        print("CAUTION: Your equipment is very heavy, you're moving slower than usual!")
    elif item_total >= 80:
        print("CAUTION: You are overloaded, can't move!")


display_inventory(stuff)
