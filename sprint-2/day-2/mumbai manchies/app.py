
import main

runProgram = True

flag = True

order = []

total = 0

userName = input(" Enter you name :--  ")

role = ""

while runProgram:
    menu = main.readmenu()
    allMenuIds = set(item["id"] for item in menu)
    if role == "" or role not in ("staff", "Staff", "student", "Student"):
        role = input("Are you Staff or Student  ")

    if role == "Staff" or role == "staff":
        if flag:
            print(f"Welcome {userName}!!")
            flag = False

        print("\n")
        print("Enter 0 to see all Snacks")
        print("Enter 1 to add Snack")
        print("Enter 2 to update availability")
        print("Enter 3 to remove Snack")
        print("Enter 4 to exit app")

        action = int(input("Enter the key--  "))

        if action == 0:
            print("\n")
            print("ID--Title--Price--Availability")
            for item in menu:
                id = item["id"]
                title = item["title"]
                price = item["price"]
                if int(item["stock"]) > 0:
                    avalible = "Y"
                else:
                    avalible = "N"
                print(f"{id}--{title}--{price}--{avalible}")
        elif action == 1:
            snackName = input("Enter the Snack Name-- ")
            snackId = input("Enter the Snack ID-- ")
            snackavailability = input("Enter the availability-- ")
            snackPrice = input("Enter the Snack Price-- ")

            addsnack = main.AddNewSnack(
                snackName, snackId, snackavailability, snackPrice, allMenuIds, menu
            )
            if addsnack:
                print("Snack is Added to Menu")
            else:
                print("Enter Valid Snack ID")
        elif action == 2:
            snackId = int(input("Enter the Snack ID-- "))
            snackavailability = int(input("Enter the availability-- "))
            update = main.updateStock(snackId, snackavailability, menu)
            if update:
                print("Snack Availability Updated")
            else:
                print("Enter Valid Snack ID")

        elif action == 3:
            print("\n")
            print("ID--Title--Price--Availability")
            for item in menu:
                id = item["id"]
                title = item["title"]
                price = item["price"]
                if int(item["stock"]) > 0:
                    avalible = "Y"
                else:
                    avalible = "N"
                print(f"{id}--{title}--{price}--{avalible}")
            snackId = int(input("Enter the Snack ID-- "))
            remove = main.removeSnack(snackId, menu)
            if remove:
                print("Snack  Removed")
            else:
                print("Enter Valid Snack ID")
        elif action == 4:
            runProgram = False
        else:
            print("Enter the Valid Key-- ")
    elif role == "student" or role == "Student":
        if flag:
            print(f"Welcome {userName} to Mumbai Manchies!!")
            flag = False

        print("\n")
        print("Enter 0 to see all Snacks")
        print("Enter 1 to buy Snacks")
        print("Enter 2 to see Bill")
        print("Enter 3 to pay bill")
        print("Enter 4 to quit app")

        action = int(input("Enter the key--  "))

        if action == 0:
            print("\n")
            print("ID--Title--Price--Availability")
            for item in menu:
                id = item["id"]
                title = item["title"]
                price = item["price"]
                if int(item["stock"]) > 0:
                    avalible = "Y"
                else:
                    avalible = "N"
                print(f"{id}--{title}--{price}--{avalible}")
        elif action == 1:
            print("\n")
            print("ID--Title--Price--Availability")
            for item in menu:
                id = item["id"]
                title = item["title"]
                price = item["price"]
                stock = item["stock"]
                print(f"{id}--{title}--{price}--{stock}")

            print("\n")
            snackId = int(input("Enter the Snack ID-- "))
            quantity = int(input("Enter the quantity you want--  "))
            placeorder = main.placeOrder(snackId, quantity, menu)
            if placeorder:
                order.append({"id": snackId, "quantity": quantity})
            else:
                print("Please Enter a valid ID")
        elif action == 2:
            bill = 0
            print('========BILL=======')
            print(f"Customer Name: {userName}")
            for item in menu:
                for snackitem in order:
                    if item["id"] == snackitem["id"]:
                        snack = item["title"]
                        price = item["price"]
                        quantity = snackitem["quantity"]
                        bill += price  * quantity
                        print(f"{snack}  ₹{price}  {quantity}")
            print(f"Total = {bill}")
            total = bill;
            print("===================")
            print("\n")
        elif action ==3 :
            if total==0:
                print("You have purchase any Snacks yet!!")
            else:
                print(f'Thank you! {userName} for paying {total}')
        elif action == 4:
            runProgram = False

    else:
        print("Enter the valid role")


if (role=='student' or role == "Student") and total>0:
    print("You will get your order soon..")
