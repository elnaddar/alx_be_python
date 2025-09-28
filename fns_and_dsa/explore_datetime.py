import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formated_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formated_date}")

def calculate_future_date():
    future_date = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.timedelta(future_date)
    current_date = datetime.datetime.now() + future_date
    formated_date = current_date.strftime("%Y-%m-%d")
    print(f"Future date: {formated_date}")
    
display_current_datetime()
calculate_future_date()