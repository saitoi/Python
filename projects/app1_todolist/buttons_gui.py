import PySimpleGUI as sg

if ''

column_layout = [[sg.Button(f'Button {i}') for i in range(20)]]

# Create a column with the layout, make it scrollable
column = sg.Column(column_layout, scrollable=True, vertical_scroll_only=True, size=(200, 150), background_color='lightgrey')

# Main window layout that includes the column
layout = [
    [sg.Text('Scrollable Column Example')],
    [column],
    [sg.Button('Exit')]
]

# Create the window
window = sg.Window('Window with a Scrollable Column', layout)

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()
