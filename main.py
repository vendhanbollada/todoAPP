import function
while True:
    user_input = input("Enter the add show edit  and then the todo name:")
    user_input = function.wording(user_input)
    todo = user_input[4:]

    if "add" in user_input:
        todos = function.file_open()


        todos.append(todo + "\n")

        function.file_write(todos)

        print(f"{todo} has been added to your list")

    elif "show" in user_input:
        todos = function.file_open()
        for index , todo in enumerate(todos):
            print(f"{index + 1}. {todo.strip("\n")}")

    elif "edit" in user_input:
        todos = function.file_open()
        for index , todo in todos:
            todo = todo.strip("")
            print(f"{index + 1}. {todo}")
        try:
            user_wants = input("enter whether you want remove replace or compelteld a todo ")
            user_wants = function.wording(user_wants)
            if "remove" or "completle" in user_wants():
                number = int(input("enter the number of todo you want to remove"))
                todos = function.file_open()
                removed_todos = todos.pop(number -1)
                function.file_write(todos)
                if "remove" in user_wants():
                   print(f'{removed_todos}is removed')
                if "completle" in user_wants():
                    print(f'{removed_todos}is completled')

            elif "replace" in user_wants:
                todos = function.file_open()
                user_number = int(input("enter the number of the todos you want to replace"))
                replaced_todos  = input("enter the todo you want to replace")
                todos[user_number -1] = replaced_todos
                function.file_write(todos)
        except SyntaxError:
            print("Pls enter a valid input")
    else :
        print("Pls enter a valid input")

    print("thank you for using the program")



