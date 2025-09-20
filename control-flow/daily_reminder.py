task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound?  (yes/no): ")
start = "Note: "
end = ""

match priority:
    case "high":
        start = "Remainder: "
    case "medium":
        start = "Attention: "

if time_bound == "no":
    end = ". Consider completing it when you have free time."
else:
    end = " that requires immediate attention today!"

print(f"{start}'{task}' is a {priority} priority task{end}")