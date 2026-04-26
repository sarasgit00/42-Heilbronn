import sys


def main():
    print("=== Inventory System Analysis ===")

    args = sys.argv[1:]
    if len(args) == 0:
        print("No inventory data provided.")
        return

    # parse arguments into inventory dict
    inventory = dict()
    for arg in args:
        parts = arg.split(":")
        if len(parts) != 2:
            print("Invalid format:", arg)
            continue
        name = parts[0]
        try:
            quantity = int(parts[1])
        except ValueError:
            print("Invalid quantity:", parts[1])
            continue

        current = inventory.get(name, 0)
        inventory.update({name: current + quantity})

    # totals
    total_items = 0
    for quantity in inventory.values():
        total_items += quantity

    print("Total items in inventory:", total_items)
    print("Unique item types:", len(inventory))

    print()
    print("=== Current Inventory ===")
    for name in inventory.keys():
        quantity = inventory.get(name)
        percent = (quantity * 100) // total_items  # integer percentage
        unit_word = "unit" if quantity == 1 else "units"
        print(name + ": " + str(quantity) + " " + unit_word +
              " (" + str(percent) + "%)")

    # find most and least abundant
    most_quantity = -1
    least_quantity = 1000000
    most_name = ""
    least_name = ""
    for name, quantity in inventory.items():
        if quantity > most_quantity:
            most_quantity = quantity
            most_name = name
        if quantity < least_quantity:
            least_quantity = quantity
            least_name = name

    print()
    print("=== Inventory Statistics ===")
    print("Most abundant: " + most_name +
          " (" + str(most_quantity) + " units)")
    print("Least abundant: " + least_name +
          " (" + str(least_quantity) + " unit)")

    # categories
    moderate = dict()
    scarce = dict()
    for name, quantity in inventory.items():
        if quantity >= 5:
            moderate.update({name: quantity})
        else:
            scarce.update({name: quantity})

    print()
    print("=== Item Categories ===")
    print("Moderate:", moderate)
    print("Scarce:", scarce)

    # restock suggestion
    restock = ""
    for name, quantity in inventory.items():
        if quantity <= 1:
            if restock != "":
                restock += ", "
            restock += name

    print()
    print("=== Management Suggestions ===")
    if restock != "":
        print("Restock needed: " + restock)
    else:
        print("Restock needed: none")

    # dictionary properties demo

    print()
    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", ", ".join(inventory.keys()))
    values_str = ""
    for v in inventory.values():
        if values_str != "":
            values_str += ", "
        values_str += str(v)
    print("Dictionary values:", values_str)
    print("'sword' in inventory:", "sword" in inventory)


if __name__ == "__main__":
    main()
