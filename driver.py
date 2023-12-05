from shoppinglistCSH import shoppinglist

def list_foodCSH():
    food_list = []
    number_of_items = int(input("Enter number of items"))

    while number_of_items <= 0:
        print(f"Number of items atleast 1")
        number_of_items = int(input("Enter number of items"))

    for repetitions in range(number_of_items):
        item = str(input("Enter item name: "))
        item_pound = float(input("Amount of pound in item: "))
        food_list.append(shoppinglist(item,item_pound))

    return (food_list)

def display_food_listCSH(food_list):
    print(f"Here's a summary of the items purchased:\n-------------------------------------------\n")
    i = 0
    for food_data in (food_list):
        print(f"Item #{i+1}-")
        print(f"Item: {food_data.food}")
        print(f"Amount: {food_data.amount} pounds")
        print(f"Price/Pound: ${food_data.std_price:.2f}")
        print(f"Cost ordered food: ${food_data.cost_orderedfood:.2f}\n")
        i+=1
        
def total_cost_all_itemCSH(food_list):
    total_cost = 0
    for food_data in (food_list):
        total_cost+= food_data.cost_orderedfood
    print(f"Total cost: ${total_cost:.2f}")
    return total_cost

def main_function():
    food_list = list_foodCSH()
    display_food_listCSH(food_list)
    total_cost_all_itemCSH(food_list)

main_function()