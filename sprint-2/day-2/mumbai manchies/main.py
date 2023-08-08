import json


def readmenu():
    with open("./menu.json", "r") as file:
        content = json.load(file)
        return content


def writemenu(menu):
    with open("./menu.json", "w") as file:
        json.dump(menu, file)




# check if that snak is already present or not
def AddNewSnack(snackName, SnackId, Avalabity, snackPrice,allMenuIds,menu):
    if SnackId in allMenuIds:
        return False
    snack = {"id": int(SnackId), "title": snackName, "price": int(snackPrice), "stock": int(Avalabity)}
    menu.append(snack)
    writemenu(menu)
    return True




def removeSnack(snackid,menu):
    newMenu = []
    for index, item in enumerate(menu):
        if item["id"] != snackid:
            newMenu.append(item)
    if len(newMenu) != len(menu):
        writemenu(newMenu)
        return True;
    else:
        return False


def updateStock(snackid, quantity,menu):
    for index, item in enumerate(menu):
        if item["id"] == snackid:
            item["stock"] = quantity
            writemenu(menu)
            return True

    return False


def placeOrder(snackid, quantity,menu):
    newMenu = []
    flag = False
    for index, item in enumerate(menu):
        if item["id"] == snackid:
            if item["stock"]<quantity:
                print("You have Enter the quantity Which is more than its availability")
                return False;
            item["stock"] -= quantity
            newMenu.append(item)
            flag = True
        else:
            newMenu.append(item)
    if flag:
        writemenu(newMenu)
        return True
    else:
        return False



    
