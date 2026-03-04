data_dict = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 1,
                "quantum_ring": 3,
            },
            "total_value": 1875,
            "item_count": 6,
        },
        "bob": {
            "items": {"code_bow": 3, "pixel_sword": 2},
            "total_value": 900,
            "item_count": 5,
        },
        "charlie": {
            "items": {"pixel_sword": 1, "code_bow": 1},
            "total_value": 350,
            "item_count": 2,
        },
        "diana": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 3,
                "health_byte": 3,
                "data_crystal": 3,
            },
            "total_value": 4125,
            "item_count": 12,
        },
    },
    "catalog": {
        "pixel_sword": {"type": "weapon", "value": 150, "rarity": "common"},
        "quantum_ring": {"type": "accessory", "value": 500, "rarity": "rare"},
        "health_byte": {"type": "consumable", "value": 25, "rarity": "common"},
        "data_crystal": {"type": "material",
                         "value": 1000, "rarity": "legendary"},
        "code_bow": {"type": "weapon", "value": 200, "rarity": "uncommon"},
    },
}

# Display inventory


def display_inventory(player: str, data: dict) -> None:
    """
    Display a player's inventory with detailed item information.

    Retrieves the player's items from the data structure, computes the total
    inventory value and item count, groups items by category, and prints a
    formatted summary including item details and category distribution.
    """

    players = data.get("players")  # dictionary of players

    catalog = data.get("catalog")  # dictionary of catalog

    inv = players[player]["items"]  # dictionary of the items of of the player

    print(f"\n=== {player.capitalize()}'s Inventory ===")

    total_value = 0
    total_items = 0
    categories = {}

    for item, qty in inv.items():

        info = catalog.get(item)

        value = info["value"]
        rarity = info["rarity"]
        item_type = info["type"]

        subtotal = qty * value
        total_value += subtotal
        total_items += qty

        categories[item_type] = categories.get(item_type, 0) + qty

        print(
            f"{item} ({item_type}, {rarity}): "
            f"{qty}x @ {value} gold each = {subtotal} gold"
        )

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    temp = []
    for k, v in categories.items():
        temp.append(f"{k}({v})")

    cat_line = ", ".join(temp)
    print(f"Categories: {cat_line}")


# Transfer items


def transfer(data: dict,
             giver: str,
             receiver: str,
             item: str,
             qty: int) -> None:
    """
    Transfer a quantity of an item from one player to another.

    Updates both inventories if the giver has sufficient quantity;
    otherwise, the transaction is cancelled.
    """

    players = data["players"]

    giver_items = players[giver]["items"]
    receiver_items = players[receiver]["items"]

    if giver_items.get(item, 0) < qty:
        print("Transaction failed!")
        return

    remain = giver_items[item] - qty
    data["players"][giver]["items"].update({item: remain})

    receiver_items[item] = receiver_items.get(item, 0) + qty

    if giver_items.get(item) == 0:
        giver_items.pop(item)

    if receiver_items.get(item) == 0:
        receiver_items.pop(item)

    print("Transaction successful!")


# Analytics


def analytics(data: dict) -> None:
    """
    Analyze player inventories to identify top statistics.

    Calculates the most valuable player, the player with the most items,
    and lists all rare items present across inventories.
    """

    players = data.get("players")
    catalog = data.get("catalog")

    richest = ""
    max_value = 0

    most_items_player = ""
    max_items = 0

    rare_items = {}

    for name, pdata in players.items():

        value = 0
        count = 0

        for item, qty in pdata["items"].items():

            value += qty * catalog[item]["value"]

            count += qty

            if catalog[item]["rarity"] == "rare":
                rare_items[item] = True

        if value > max_value:
            max_value = value
            richest = name

        if count > max_items:
            max_items = count
            most_items_player = name

    print("\n=== Inventory Analytics ===")
    print(f"Most valuable player: "
          f"{richest.capitalize()} ({max_value} gold)")
    print(f"Most items: "
          f"{most_items_player.capitalize()} ({max_items} items)")

    print("Rarest items:", ", ".join(rare_items.keys()))


# MAIN


def main():
    """
    Run the inventory system workflow.

    Displays a player's inventory, performs an item transfer between
    players, shows updated results, and executes inventory analytics
    with basic exception handling.
    """

    print("=== Player Inventory System ===")
    player = "alice"

    giver = "alice"
    receiver = "bob"

    item = "health_byte"
    qty = 0
    try:

        display_inventory(player, data_dict)

        print(
            f"\n=== Transaction: {giver.capitalize()}"
            + f"gives {receiver.capitalize()} {qty} {item} ==="
        )
        transfer(data_dict, giver, receiver, item, qty)

        print("\n=== Updated Inventories ===")
        print(
            f"{giver.capitalize()} health_byte:",
            data_dict["players"][giver]["items"].get(item, 0),
        )
        print(
            f"{receiver.capitalize()} health_byte:",
            data_dict["players"][receiver]["items"].get(item, 0),
        )

        analytics(data_dict)

    except Exception as E:
        print("Key Error: ", E)


if __name__ == "__main__":
    main()
