import sys


inventory: dict = dict()
total: int = 0
unique_count: int = 0
error_occurred: bool = False

try:
    inventory: dict = dict()
    for av in sys.argv[1:]:
        name, quantity = av.split(':')
        if quantity < '0':
            raise ValueError("quantity can't be negative!")
        inventory[name] = int(quantity)
    for val in inventory.values():
        total += val
    items: list = list(inventory.items())
    keys: list = list(inventory.keys())
    unique_count: int = len(inventory)
    values: list = list(inventory.values())
except Exception as er:
    print(f"Error: {er}")
    error_occurred = True


def system_analysis() -> None:
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {unique_count}")


def current_inventory() -> None:
    print("\n=== Current Inventory ===")
    n: int = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j+1] = items[j+1], items[j]
    for key, val in items:
        print(f"{key}: {val} units ({((val / total) * 100):.1f})%")


def statistics() -> None:
    print("\n=== Inventory Statistics ===")
    key, val = items[0][0], items[0][1]
    print(f"Most abundant: {key} ({val} units)")
    minn = min(values)
    for key, val in items:
        if minn == val:
            print(f"Least abundant: {key} ({val} units)")


def categories() -> None:
    print("\n=== Item Categories ===")
    new: dict = {
        "Moderate": {},
        "Scarce": {}
    }
    for key, v in items:
        if v >= 5:
            new["Moderate"][key] = v
        else:
            new["Scarce"][key] = v
    print(f"Moderate: {new["Moderate"]}")
    print(f"Scarce: {new["Scarce"]}")


def management_suggestions() -> None:
    print("\n=== Management Suggestions ===")
    new: list = []
    for key, v in items:
        if v <= 1:
            new.append(key)
    result: str = "Restock needed: "
    for i in range(len(new)):
        result += new[i]
        if i < len(new) - 1:
            result += ", "
    print(result)


def properties_demo() -> None:
    print("\n=== Dictionary Properties Demo ===")
    res1: str = "Dictionary keys: "
    res2: str = "Dictionary values: "
    for i in range(len(keys)):
        res1 += keys[i]
        if i < len(keys) - 1:
            res1 += ", "
    for j in range(len(values)):
        res2 += str(values[j])
        if j < len(values) - 1:
            res2 += ", "
    print(res1)
    print(res2)
    print(f"Sample lookup - 'sword' in inventory: "
          f"{inventory.get("sword") is not None}")


def main() -> None:
    if error_occurred:
        return
    try:
        if len(sys.argv) > 1:
            print("=== Inventory System Analysis ===")
            system_analysis()
            current_inventory()
            statistics()
            categories()
            management_suggestions()
            properties_demo()
        else:
            print("Error: You need at least one argument!")
            print(f"Usage: python3 {sys.argv[0]} <item:quantity> ...")
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
