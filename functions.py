FILEPATH=r"todos.txt"
# Ez a felső a relatív, de megadhatom abszolútban is: r"C:\Users\Random\Documents\PycharmProjects\files\todos.txt"

def get_todos(filepath=FILEPATH):
    """Read the text file and return the list of to-do items"""
    #To Watch all the docstrings: right click on a function -> go to -> implementation
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local
#Vagy így:
#print(help(get_todos))

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__=="__main__":
    print(__name__)