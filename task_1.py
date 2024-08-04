import pulp

# Створення проблеми
problem = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Змінні
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Обмеження
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
problem += 1 * lemonade <= 50, "Sugar"
problem += 1 * lemonade <= 30, "Lemon Juice"
problem += 2 * fruit_juice <= 40, "Fruit Puree"

# Цільова функція
problem += lemonade + fruit_juice, "Total Products"

# Розв'язання задачі
problem.solve()

# Вивід результатів
print("Status:", pulp.LpStatus[problem.status])
print("Lemonade produced:", pulp.value(lemonade))
print("Fruit Juice produced:", pulp.value(fruit_juice))
print("Total Products produced:", pulp.value(problem.objective))
