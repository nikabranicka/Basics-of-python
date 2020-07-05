import pyinputplus as pyip

BREAD_TYPE_AND_PRICE = {"Wheat Bread": 5, "White Bread": 4, "Sourdough Bread": 6}
PROTEIN_TYPE_AND_PRICE = {"Chicken": 5, "Turkey": 6, "Ham": 4, "Tofu": 5}
CHEESE_TYPE_AND_PRICE = {"Cheddar": 5, "Swiss": 6, "Mozzarella": 7}
SAUCE_TYPE_AND_PRICE = {"Mayo": 1, "Mustard": 2, "Lettuce": 3, "Tomato": 4}


def select_bread():
    print("What kind of bread do you prefer?")
    bread_type_list = list(BREAD_TYPE_AND_PRICE.keys())
    selected_bread_type = pyip.inputMenu(bread_type_list, lettered=True)
    return {selected_bread_type: BREAD_TYPE_AND_PRICE[selected_bread_type]}


def select_protein():
    print("What kind of protein do you prefer?")
    protein_type_list = list(PROTEIN_TYPE_AND_PRICE.keys())
    selected_protein_type = pyip.inputMenu(protein_type_list, lettered=True)
    return {selected_protein_type: PROTEIN_TYPE_AND_PRICE[selected_protein_type]}


def select_cheese():
    print("Do you want cheese?")
    with_cheese = pyip.inputYesNo()
    if with_cheese == 'yes':
        print("What kind of cheese do you prefer?")
        cheese_type_list = list(CHEESE_TYPE_AND_PRICE.keys())
        selected_cheese_type = pyip.inputMenu(cheese_type_list, lettered=True)
        return {selected_cheese_type: CHEESE_TYPE_AND_PRICE[selected_cheese_type]}
    return None


def select_sauce():
    print("Do you want sauce?")
    with_sauce = pyip.inputYesNo()
    if with_sauce == 'yes':
        print("What kind of sauce do you prefer?")
        sauce_type_list = list(SAUCE_TYPE_AND_PRICE.keys())
        selected_sauce_type = pyip.inputMenu(sauce_type_list, lettered=True)
        return {selected_sauce_type: SAUCE_TYPE_AND_PRICE[selected_sauce_type]}
    return None


def make_sandwich():
    print("Welcome to sandwich maker! Please choose your ingredients")
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
