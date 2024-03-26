import todo_list_func as todo
import PySimpleGUI as sg

bg_color = 'white'
text_color = 'black'

# Assuming todo.actions is a dictionary mapping action names to functions
menu_actions = list(todo.actions.keys())
# Assuming todo.get_todo() returns a list of current to-do items
todo_list = todo.get_todo()

main_column = sg.Column([
    [sg.Listbox(values=menu_actions,
                key='-MENU_ACTIONS-',
                text_color=text_color, background_color=bg_color,
                select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,
                expand_x=True, expand_y=True,
                enable_events=True, size=(20, len(menu_actions))),
    sg.Listbox(values=todo_list,
                key='-TODO_LIST-',
                text_color=text_color, background_color=bg_color,
                expand_x=True, expand_y=True,
                enable_events=True, size=(20, len(todo_list)))]
])

layout = [
    [main_column],
    [sg.Text('Type task description and select an action:', background_color=bg_color, text_color=text_color, expand_x=True)],
    [sg.InputText(tooltip='Enter a task', key='-TASK-', expand_x=True), sg.Button('Submit', bind_return_key=True, button_color=(text_color, bg_color))]
]

mainwindow = sg.Window('To-do App', layout=layout, background_color=bg_color,
                       resizable=True, finalize=True, font=('Helvetica', 20))

# Event Loop
while True:
    event, values = mainwindow.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Submit':
        selected_action = values['-MENU_ACTIONS-'][0] if values['-MENU_ACTIONS-'] else None
        task_description = values['-TASK-']
        if selected_action and task_description:
            # Call the selected action function with task_description
            # Assuming the function signature matches what's needed
            todo.actions[selected_action](todo.file_path, task_description)
            # Refresh the todo_list to reflect any changes
            todo_list = todo.get_todo()  # Re-fetch the updated list
            mainwindow['-TODO_LIST-'].update(todo_list)  # Update the Listbox
            mainwindow['-TASK-'].update('')  # Clear input after action

mainwindow.close()
