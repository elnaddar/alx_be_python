m_income = int(input("Enter your monthly income: "))
m_expenses = int(input("Enter your total monthly expenses: "))

m_savings = m_income - m_expenses
print(f"Your monthly savings are ${m_savings}.")

p_savings = m_savings * 12 + m_savings * 12 * 0.05
print(f"Projected savings after one year, with interest, is: ${p_savings}.")