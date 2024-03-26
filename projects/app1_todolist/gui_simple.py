import PySimpleGUI as sg

# Vars
bg_color = 'white'

# Simple layout
layout = [
    [sg.Text('Enter task (action + description):')],
    [sg.InputText()],
    [sg.Button('Submit', bind_return_key=True)]
]

# Create and read from the window in one line
event, values = sg.Window('To-do App', layout, background_color=bg_color).read(close=True)

# Process the input
if event == 'Submit':
    input_text = values[0]  # Assuming the input field is the first element
    # Here, you could process the input_text, such as splitting it into action and task
    print(f"Received input: {input_text}")  # Placeholder for actual processing
