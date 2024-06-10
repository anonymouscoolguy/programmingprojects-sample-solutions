print("==== Krusty Krab Tip Calculator ====")
print("Meal price (in $): ", end="")
meal_price = float(input())
print("Tip percentage (in %): ", end="")
percentage = float(input())

tip = meal_price*(percentage / 100)
total = meal_price + tip

print()
print("==== Receipt ====")
print(f"Meal: ${meal_price:.2f}")
print(f"Tip: ${tip:.2f}")
print("----------")
print(f"Total: ${total:.2f}")