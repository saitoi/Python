computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]
available_choices = []
my_list = []
my_choice = ""

while my_choice != '-1':
    print("Choose the computer parts listed below:")
    for i, item in enumerate(computer_parts):
        print(f"{i}: {item}")
        available_choices.append(str(i))
    my_choice = input("Your choice: ")
    if my_choice in available_choices:
        my_list.append(computer_parts[int(my_choice)])
    elif my_choice == '-1':
        print("Programa encerrando..")
    else:
        print("Por favor, selecione novamente")
print(my_list)
