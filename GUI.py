import FreeSimpleGUI as sg
import function


label = sg.Text("type in a todo")
input_box = sg.InputText(tooltip="Enter the name of the todo" , key = "todo")
list_box = sg.Listbox(values = function.file_open(), key = "todos",
                      enable_events=True , size=(45, 10))

exit_button = sg.Button("Exit", key = "exit")
add_button = sg.Button("add" , key = "add")
edit_button = sg.Button("edit" , key = "edit")
complete_button = sg.Button("complete" , key = "complete")
window = sg.Window("Todo-App List" , layout=[[label , add_button] , [input_box] ,[list_box , edit_button , complete_button], [exit_button]], font= ("Helvetica", 14))

whileTrue:
    event , values = window.read()
    print(values, event)
    match event:
        case "add":
            todos = function.file_open()
            new_todos = values["todo"] + "\n"
            todos.append(new_todos)
            function.file_write(todos)
            window["todos"].update(values = todos)
        case "edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = function.file_open()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.file_write(todos)
            window["todos"].update(values = todos)
        case "complete":
            todo_to_complete = values["todos"][0]
            todos = function.file_open()
            todos.remove(todo_to_complete)
            function.file_write(todos)
            window["todos"].update(values = todos)
            window['todo'].update(value = "")
        case 'todos':
            window["todo"].update(value=values["todos"][0])
        case 'exit':
            break
        case sg.WIN_CLOSED:
            break




window.close()
