inventory = {"laptop": 5, "mouse": 10, "keyboard": 0}
orders = [
    ("laptop", 2),
    ("mouse", 15),
    ("keyboard", 1),
    ("monitor", 3),
]

for product, qty in orders:
    match (product, qty):
        case (p, q) if p not in inventory:
            print(f"{p}: not in inventory")
            
        case (p, q) if inventory[p] >= q:
            inventory[p] -= q
            print(f"{p}: shipped {q}, {inventory[p]} left")
            
        case (p, q) if inventory[p] < q:
            print(f"{p}: only {inventory[p]} in stock, cannot ship {q}")
