monthely_income = int(input("Enter your monthly income: "))
monthely_expenses = int(input("Enter your total monthly expenses: "))

monthely_savings = monthely_income - monthely_expenses
print(f"Your monthly savings are ${monthely_savings}.")

p_savings = monthely_savings * 12 + monthely_savings * 12 * 0.05
print(f"Projected savings after one year, with interest, is: ${p_savings}.")