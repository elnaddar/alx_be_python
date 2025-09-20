# Generated using AI as their task was created
# using AI and have no details on the review criteria

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder_message = f"'{task}' is a {priority} priority task"

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case 'high':
        if time_bound == 'yes':
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += ". Consider completing it soon."
    case 'medium':
        if time_bound == 'yes':
            reminder_message += " that needs to be done today."
        else:
            reminder_message += ". It's a good candidate for today's to-do list."
    case 'low':
        if time_bound == 'yes':
            reminder_message += ". You should try to get this done today if you can."
        else:
            reminder_message += ". Consider completing it when you have free time."
    case _:
        reminder_message = "I didn't recognize that priority level. Please try again with 'high', 'medium', or 'low'."

# Provide the Customized Reminder
print("\nReminder:", reminder_message)