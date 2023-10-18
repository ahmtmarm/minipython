def billboard(name, price=30):
    if len(name) == 0:
        return 0
    else:
        total_cost = price
        total_cost += billboard(name[1:], price)
        return total_cost

name = "Ahmet Halit Marim"
cost = billboard(name)
print(f"The cost of the billboard ad for '{name}' is £{cost}")
