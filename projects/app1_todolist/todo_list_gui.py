import todo_list_func as todo
import PySimpleGUI as sg

bg_color = 'white'
text_color = 'black'

menu_actions = list(todo.actions.keys())
sg.Column([[sg.Listbox(values=menu_actions, key='-ACTIONS-',
                       enable_events=True, background_color=bg_color,
                       text_color=text_color, select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,
                       expand_x=True, expand_y=True)],
                       [sg.Listbox(expand_x=True, expand_y=True,
                        text_color=text_color, background_color=bg_color)]])

menu_layout = [
    [sg.Listbox(values=menu_actions, size=(20, len(menu_actions)), key='-ACTIONS-', enable_events=True, background_color=bg_color, text_color=text_color, select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, expand_x=True, expand_y=True)]
]

layout = [
    [sg.Frame('To-do List Menu', menu_layout, font='Any 12', title_color=text_color, background_color=bg_color, expand_x=True, expand_y=True)],
    [sg.Text('Select an action and type the task description:', background_color=bg_color, text_color=text_color, expand_x=True)],
    [sg.InputText(tooltip='Enter a task', key='-TASK-', expand_x=True), sg.Button('Submit', bind_return_key=True, button_color=(text_color, bg_color))]
]

mainwindow = sg.Window('To-do App', layout=layout, background_color=bg_color,
                       resizable=True, finalize=True, font=('Heveltica', 20))

# Expand elements
mainwindow['-ACTIONS-'].expand(expand_x=True, expand_y=True)
mainwindow['-TASK-'].expand(expand_x=True)
mainwindow['Submit'].expand(expand_x=True)

# Event Loop
while True:
    event, values = mainwindow.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Submit':
        selected_action = values['-ACTIONS-'][0] if values['-ACTIONS-'] else None
        task_description = values['-TASK-']
        if selected_action and task_description:
            todo.actions[selected_action](todo.file_path, task_description)
            mainwindow['-TASK-'].update('')

mainwindow.close()
