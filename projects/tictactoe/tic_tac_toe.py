
def menu() -> str:
    return("""
Welcome to the best Tic-tac-toe !!
----------------------------------
1. Play against a friend
2. Play against a bot
3. Exit
> """)

def print_board(l: list) -> None:
    if len(l) != 9:
        raise ValueError("A lista deve conter exatamente 9 elementos.")

    for i in range(0, 9, 3):
        if i > 0:
            print("-----------")
        print(f" {l[i]} | {l[i+1]} | {l[i+2]} ")

def against_friend():
    
    pass

def against_bot():
    pass

if __name__ == '__main__':
    values_list = [" "]*9
    option = None

    while option != '3':
        option = input(menu())
        if option == '1':

        elif option == '2':
