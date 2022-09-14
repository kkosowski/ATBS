def displayinventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(k + ':', v)
        item_total += v
    print("Total number of items: " + str(item_total))
    print('//////////////////////////////////////')


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addtoinventory(inventory, addeditems):
    for k in addeditems:
        inventory.setdefault(k, 0)
        inventory[k] += 1
    return inventory


displayinventory(inv)
inv = addtoinventory(inv, dragonLoot)
displayinventory(inv)
