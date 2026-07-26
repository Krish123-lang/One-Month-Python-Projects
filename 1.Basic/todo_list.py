todo_list = []

while True:
    user_input = input(
        '''
        1. Add items
        2. Read items
        3. View all elements
        4. Update items
        5. Delete items
        6. Exit
        '''
    )

    if user_input == "1":
        input_elem = input("Enter the element to insert: ")
        todo_list.append(input_elem)

    elif user_input == "2":
        try:
            input_idx = int(input("Enter the index number to see the element: "))
            print(todo_list[input_idx])
        except Exception as e:
            print(e)
            
    elif user_input == "3":
        print(todo_list)

    elif user_input == "4":
        input_idx = int(input("Enter the index number to update the element: "))
        input_update = input("Enter the element: ")
        todo_list[input_idx] = input_update
        print(todo_list)
        
    elif user_input == "5":
        input_idx = int(input("Enter the index number to delete the element: "))
        del_elem = todo_list.pop(input_idx)
        print(f"{del_elem} was removed !")
        
    elif user_input == "6":
        print("Bye Bye !")
        break
    
    else:
        print("Invalid !")
