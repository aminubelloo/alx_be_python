task = input("Enter your task:")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound (yes/no):")


match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        else:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound =="yes":
            print("This is a medium priority task, but it is time-bound, make sure to complete it.")
        else:
            print("This is a medium priority task but it is not time bound.")
    case "low":
        if time_bound =="yes":
            print("This is  a low priority task but it is time-bound.")
        else:
            print("This is a low priority task and it is not time-bound, sit back and sip some coffee!")
        
    case _:
        print("Invalid selection.")
