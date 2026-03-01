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
            "items": {
                "code_bow": 3,
                "pixel_sword": 2
            },
            "total_value": 900,
            "item_count": 5,
        },
        "charlie": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1
            },
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
        "data_crystal": {"type": "material", "value": 1000,
                         "rarity": "legendary"},
        "code_bow": {"type": "weapon", "value": 200, "rarity": "uncommon"},
    },
}

# Display inventory

def display_inventory(player: str, data: dict) -> None:
    players = data.get("players") # dictionary of players
    catalog = data.get("catalog") # dictionary of catalog

    inv = players[player]["items"] #dictionary of the items of of the player
    # inv = players[player].get("items")
    # print(inv.items())
    
    print(f"\n=== {player.capitalize()}'s Inventory ===")

    total_value = 0
    total_items = 0
    categories = {}

    for item, qty in inv.items():
        # print(item)
        # print(qty)

        info = catalog.get(item)

        value = info["value"]
        rarity = info["rarity"]
        item_type = info["type"]

        subtotal = qty * value
        total_value += subtotal
        total_items += qty

        categories[item_type] = (
            categories.get(item_type, 0) + qty
        )
        # print(categories)

        print(
            f"{item} ({item_type}, {rarity}): "
            f"{qty}x @ {value} gold each = {subtotal} gold"
        )

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    cat_line = ", ".join(
        f"{k}({v})" for k, v in categories.items()
    )
    print(f"Categories: {cat_line}")


# -------------------------------------------------
# Transfer items
# -------------------------------------------------
def transfer(data: dict,
             giver: str,
             receiver: str,
             item: str,
             qty: int) -> None:

    players = data["players"]
    print(players)

    giver_items = players[giver]["items"]
    receiver_items = players[receiver]["items"]

    if giver_items.get(item, 0) < qty:
        print("Transaction failed!")
        return

    # giver_items[item] -= qty
    last = giver_items[item] - qty 
    data["players"][giver]["items"][item] = last

    receiver_items[item] = (
        receiver_items.get(item, 0) + qty
    )

    if giver_items.get(item) == 0:
        # del (data["players"][giver]["items"][item])
        del(giver_items[item])
    print("Transaction successful!")


# -------------------------------------------------
# Analytics
# -------------------------------------------------
def analytics(data: dict) -> None:
    players = data.get("players")
    catalog = data.get("catalog")

    richest = ""
    max_value = 0

    most_items_player = ""
    max_items = 0

    rare_items = {}
    # print()
    # print(players.items())
    # print()
    for name, pdata in players.items():
        # print(name)
        # print(pdata)

        value = 0
        count = 0
        # print(pdata["items"])
        # print()
        # print(pdata["items"].items())
        for item, qty in pdata["items"].items():
            # print(item)
            # print()
            # print(qty)
            # print()
            value += qty * catalog[item]["value"]
            # print(value)
            # print()
            count += qty
            # print(count)
            # print()

            if catalog[item]["rarity"] == "rare":
                rare_items[item] = True

        if value > max_value:
            max_value = value
            richest = name
            # print(name)
        if count > max_items:
            max_items = count
            most_items_player = name
            # print(name)
            # print()
    print("\n=== Inventory Analytics ===")
    print(
        f"Most valuable player: "
        f"{richest.capitalize()} ({max_value} gold)"
    )
    print(
        f"Most items: "
        f"{most_items_player.capitalize()} ({max_items} items)"
    )
    print(rare_items)
    # print("Rarest items:", ", ".join(rare_items.keys()))
    print("Rarest items:" , ", ".join(rare_items.keys()))
    



# -------------------------------------------------
# MAIN
# -------------------------------------------------
def main():
    print("=== Player Inventory System ===")
    try :

        display_inventory("alice", data_dict)

        print("\n=== Transaction: Alice gives Bob 2 health_byte ===")
        transfer(data_dict, "alice", "bob", "health_byte", 1)

        print("\n=== Updated Inventories ===")
        print(
            "Alice health_byte:",
            data_dict["players"]["alice"]["items"].get("health_byte")
        )
        print(
            "Bob health_byte:",
            data_dict["players"]["bob"]["items"].get("health_byte")
        )

        analytics(data_dict)

        display_inventory("alice", data_dict)

    except Exception as E:
        print("Key Error: ",E)


if __name__ == "__main__":
    main()
    # my = data_dict["players"]["alice"]["items"].items()
    # print(data_dict["players"]["alice"]["items"].items())
    # print(type(my))

    # my_dict = {}

    # my_dict["good"] = 1
    # print(my_dict)
    # my_dict["goo"] = 2
    # print(my_dict)
    # # my_dict = data_dict["players"]["alice"].get('items')
    # # print(my_dict)
    # # print(type(my_dict))
    # # an_dict = data_dict["players"]["alice"]["items"]
    # # print(an_dict)
    # # print(type(an_dict))
    # my = data_dict.get("catalog") 
    # print(my)
    # print(type(my))
    # print()
    # other = data_dict["catalog"].items()
    # print(other)
    # print(type(other))
    # t = ('a' , 1 , 2)
    # x  = t
    # print(x )
    # dict = {"key1" : 1 , "key2" : 2}
    # # print(dict.items())
    # a = dict.items()
    # for x in  a : # (key, 1) (key, 2)
    #     # print(len(dict.items()))
    #     print(a)
    #     print(x)