customers = [
    {"name": "SpaceX", "employees": 1029, "industry": "Space"},
    {"name": "Google", "employees": 457855, "industry": "Software"},
    {"name": "Tinder", "employees": 654, "industry": "Dating"},
]

print(customers[1]["employees"])

for customer in customers:
    print(
        f"Customer {customer['name']} has {customer['employees']} employees and is a leading in the {customer['industry']} industry"
    )
