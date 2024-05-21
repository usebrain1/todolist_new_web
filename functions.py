FILEPATH = 'todos.txt'

def get_todos(filepath = FILEPATH):
    """
    Read a file path and return the list of to-do items.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

### print(help(get_todos))

def write_todos(todos_arg, filepath = FILEPATH):
    """
    Write the to-do items list in text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)