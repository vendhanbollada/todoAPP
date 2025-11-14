def wording(string):
    string = string.lower()
    string = string.strip()
    return string


def file_open():
    with open("todos.txt" , "r") as file:
        todos_local = file.readlines()
    return todos_local


def file_write(todos):
    with open("todos.txt", "w") as file:
        file.writelines(todos)