def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
    elif unit == "area":
        message = f"covers {quantity} square meters"
        print(f"{seed_type.capitalize()} seeds: {message}")
    else:
        print("Unknown unit type")
