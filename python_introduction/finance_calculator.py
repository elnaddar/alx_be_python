monthly__income = int(input("Enter your monthly income: "))
monthly__expenses = int(input("Enter your total monthly expenses: "))

monthly__savings = monthly__income - monthly__expenses
print(f"Your monthly savings are ${monthly__savings}.")

p_savings = monthly__savings * 12 + monthly__savings * 12 * 0.05
print(f"Projected savings after one year, with interest, is: ${p_savings}.")