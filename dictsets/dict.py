# Adding items to a shopping list

avaliable_parts = {
    "1": "Computer",
    "2": "Monitor",
    "3": "Keyboard",
    "4": "Mouse",
    "5": "Mouse Mat",
    "6": "HDMI Cable",
}

current_choice = None
shopping_list = {}

while current_choice != "0":
    if current_choice in avaliable_parts:
        chosen_part = avaliable_parts[current_choice]
        if chosen_part in shopping_list:
            # Item already in the list, so remove it
            print(f"Removing item {chosen_part} from the list")
            shopping_list.pop(chosen_part)
        else:
            print(f"Adding {avaliable_parts[current_choice]}")
            shopping_list[current_choice] = chosen_part
    else:
        print("Please add options from the list below:")
        for key, value in avaliable_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")
