import pyinputplus as pyip

bread_type_and_price = {"Wheat Bread": 5, "White Bread": 4, "Sourdough Bread": 6}
protein_type_and_price = {"Chicken": 5, "Turkey": 6, "Ham": 4, "Tofu": 5}
cheese_type_and_price = {"Cheddar": 5, "Swiss": 6, "Mozzarella": 7}
sauce_type_and_price = {"Mayo": 1, "Mustard": 2, "Lettuce": 3, "Tomato": 4}

print("Welcome to sandwich maker! Please choose your ingredients")


def select_bread():
    print("What kind of bread do you prefer?")
    bread_type_list = list(bread_type_and_price.keys())
    selected_bread_type = pyip.inputMenu(bread_type_list, lettered=True)
    return {selected_bread_type: bread_type_and_price[selected_bread_type]}


def select_protein():
    print("What kind of protein do you prefer?")
    protein_type_list = list(protein_type_and_price.keys())
    selected_protein_type = pyip.inputMenu(protein_type_list, lettered=True)
    return {selected_protein_type: protein_type_and_price[selected_protein_type]}


def select_cheese():
    print("Do you want cheese?")
    with_cheese = pyip.inputYesNo()
    if with_cheese == 'yes':
        print("What kind of cheese do you prefer?")
        cheese_type_list = list(cheese_type_and_price.keys())
        selected_cheese_type = pyip.inputMenu(cheese_type_list, lettered=True)
        return {selected_cheese_type: cheese_type_and_price[selected_cheese_type]}


def select_sauce():
    print("Do you want sauce?")
    with_sauce = pyip.inputYesNo()
    if with_sauce == 'yes':
        print("What kind of sauce do you prefer?")
        sauce_type_list = list(sauce_type_and_price.keys())
        selected_sauce_type = pyip.inputMenu(sauce_type_list, lettered=True)
        return {selected_sauce_type: sauce_type_and_price[selected_sauce_type]}


def make_sandwich():
    sandwich = {}
    sandwich.update(select_bread())
    sandwich.update(select_protein())
    selected_cheese = select_cheese()
    if selected_cheese is not None:
        sandwich.update(selected_cheese)
    selected_sauce = select_sauce()
    if selected_sauce is not None:
        sandwich.update(selected_sauce)
    return sandwich


def sum_up_order(ordered_sandwich: dict):
    """
    Method responsible for mapping from ingredients names to their prices and printing the sandwich
    content along with total price for selected amount of sandwiches.
    """
    print("How many sandwiches do you want to order?")
    number_of_sandwiches = pyip.inputInt(min=1)
    total_price = sum(ordered_sandwich.values()) * number_of_sandwiches
    print(
        f"Your sandwich consist of {', '.join(ordered_sandwich.keys())}. You wanted {number_of_sandwiches}."
        f" That's a total of {total_price} eur")


prepared_sandwich = make_sandwich()
sum_up_order(prepared_sandwich)
