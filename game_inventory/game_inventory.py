
def display_inventory(inventory):
    print("INVENTORY")
    total=0
    for key, value in inventory.items():
        print(f'{value} {key}')
        total+=value
    print(f"Total Number Of Items: {total}")
    
def add_to_inventory(inventory, added_items):
    set_list=set(added_items)
    for item in set_list:
        if item in inventory:
            inventory[item]+=added_items.count(item)
        else:
            inventory[item]=added_items.count(item)
    display_inventory(inventory)
    
def main():
    d={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#display_inventory(d)
    add_to_inventory(d, dragonLoot)

if "__main__"==__name__:
    main()