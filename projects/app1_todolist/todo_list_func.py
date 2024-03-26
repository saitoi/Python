file_path = 'todo_list.txt'

# TODO Make todo func simpler
def todo(file='todo_list.txt'):
    option = input(menu()).lower()
    if not option.startswith('exit'):
        try:
            for key, func in actions.items():
                if option.casefold().startswith(key):
                    todo_item = option.removeprefix(key + ' ')
                    func(file, todo_item)
        except FileNotFoundError:
            with open(file, 'w', encoding='utf-8') as _:
                print(f'File {file} Not Found.. {file} Created.')
        todo()


def menu() -> str:
    return """
-----------------------
****** TO-DO LIST *****
-----------------------
Functions:
- add
- show
- edit
- complete
- exit

Type the function name + space + task description, like so:
add Clean the dishes..
> """


def add(file=file_path, todo_item='') -> None:
    if todo:
        with open(file, 'a', encoding='utf-8') as todofile:
            print(todo_item, file=todofile, end='\n')
    else:
        print("Empty todo .. Try again")


def print_list(file=file_path, todo_item='') -> None:
    with open(file, 'r', encoding='utf-8') as todofile:
        todolist = map(str.strip, todofile.readlines())
        list(map(lambda pair: print(f'{pair[0]+1}: {pair[1]}'), enumerate(todolist)))


# TODO Try and except block missing
def complete(file=file_path, todo_item=''):
    if todo_item:
        with open(file, 'r', encoding='utf-8') as read_todo:
            print_list(file)
            todolist = read_todo.readlines()
            remove_index = [index for index, item in enumerate(todolist) if todo_item in item][0]
            print('The removed index is', remove_index)
            todolist.pop(remove_index)
            overwrite_file(todolist, file)
    else:
        print('Empty todo .. Try again')


# TODO Update completed tasks
# TODO Ability to update more than one task at once
def edit(file=file_path, todo_item='') -> None:
    if todo_item:
        with open(file, 'r', encoding='utf-8') as read_todo:
            todolist = read_todo.readlines()
            if todolist:
                edit_index = [index for index, item in enumerate(todolist) if todo_item in item][0]
                new_todo = input('Type the new todo: ') + '\n'
                todolist[edit_index] = new_todo
                overwrite_file(todolist, file)
            else:
                print("File's empty .. Try again")
    else:
        print('Empty todo .. Try again')


def overwrite_file(todolist, file=file_path) -> None:
    with open(file, 'w', encoding='utf-8') as write_todo:
        write_todo.writelines(todolist)


def get_todo(file=file_path, ) -> None:
    with open(file, 'r', encoding='utf-8') as read_todo:
        todo_list = read_todo.readlines()
        return todo_list


actions = {
    'add': add,
    'show': print_list,
    'edit': edit,
    'complete': complete,
    'exit': None,
}


if __name__ == '__main__':
    todo()
