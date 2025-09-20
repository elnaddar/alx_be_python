# Generated using AI as their task was created
# using AI and have no details on the review criteria

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Start building the reminder message
reminder = f"'{task}' is a {priority} priority task"

# Use Match Case to determine the base message
match priority:
    case 'high':
        # High priority tasks
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += " that should be completed soon."
    case 'medium':
        # Medium priority tasks
        if time_bound == 'yes':
            reminder += " that needs to be done today."
        else:
            reminder += "."
    case 'low':
        # Low priority tasks
        if time_bound == 'yes':
            reminder += " that you should try to do today if you can."
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        # Handles unexpected input
        reminder = "I couldn't create a reminder for that priority level. Please try again with 'high', 'medium', or 'low'."

# Provide a customized reminder using a single print statement
print(f"Reminder: {reminder}")