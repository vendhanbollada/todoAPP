import FreeSimpleGUI as sg
import function


label = sg.Text("type in a todo")
input_box = sg.InputText(tooltip="enter the name of the todo")
add_button = sg.Button("add")
window = sg.Window("Todo-App List" , layout=[[label , add_button], [input_box]])

window.read()
window.close()
