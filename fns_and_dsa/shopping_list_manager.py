def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
        shopping_list=[]
        while True:
            display_menu()
            
            choice = input("Enter your choice:").strip()
            if not choice.isdigit():
             print("Invalid input. Please enter a number.")
             continue  # Go back to the start of the loop

             choice = int(choice)

           
            if choice == '1':
                item = input("Enter an item to add:").strip()
                shopping_list.append(item)
                print(f"{item} has been added to your shopping list.")
                
            elif choice == '2':
                item=input("Enter an item you want to remove:").strip()
                if item in shopping_list:
                     shopping_list.remove(item)
                     print(f"{item} has been removed from your shopping list.")
                else:
                     print(f"{item} does not exist in the list.")
            
            elif choice == '3':
                 if shopping_list:
                      print("\n Your shopping list:")
                      for i, item in enumerate(shopping_list,start=1):
                           print(f"{i}.{item}")
                 else:
                  print("Your shopping list is empty.")
            elif choice == '4':
                print("Goodbye")
                break
        
            else:
                 print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
