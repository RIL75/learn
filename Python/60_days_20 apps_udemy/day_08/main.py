while True:
    user_action = input("Type add, show, complete or exit \n ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos.append(todo)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            # new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number -= number

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            print('Here is todos exiting', todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)


            print('Here is how it will be', todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo{todo_to_remove} was removed from the list."
            print(message)

        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")
print("Bye!")