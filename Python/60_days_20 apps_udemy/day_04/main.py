todos =[]

while True:
    user_action = input("Type add, show, or exit \n ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number -= number
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")
print("Bye!")