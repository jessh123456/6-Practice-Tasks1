def garnishfunction(list):
    yesnorepeat = 0
    list = []
    price = 0
    garnishrepeat = 0
    while garnishrepeat != 1:
        yesnorepeat = 0
        garnish = str(input("What garnish would you like in your sandwich?"
                            "\nOnion          $1.69 (press 'O')"
                            "\nTomato         $1.00 (press 'T')"
                            "\nLettuce        $2.00 (press 'L')"
                            "\nCheese         $2.50 (press 'C')"
                            "\n: ")).upper()
        if garnish == "O":
            price += 1.69

            list.append("Onion")
            while yesnorepeat == 0:
                yesno = input("Would you like another garnish? "      
                              "('Y' for yes, 'N' for no)\n: ").upper()
                if yesno == "N":
                    garnishrepeat = 1
                    yesnorepeat = 1
                elif yesno == "Y":
                     yesnorepeat = 1
                else:
                    print("Please Enter 'Y' for yes or 'N' for no.")
        elif garnish == "T":
            price += 1.00
            list.append("Tomato")
            while yesnorepeat == 0:
                yesno = input("Would you like another garnish? "
                              "('Y' for yes, 'N' for no)\n: ").upper()
                if yesno == "N":
                    garnishrepeat = 1
                    yesnorepeat = 1
                elif yesno == "Y":
                     yesnorepeat = 1
                else:
                    print("Please Enter 'Y' for yes or 'N' for no.")
        elif garnish == "L":
            price += 2.00
            list.append("Lettuce")
            while yesnorepeat == 0:
                yesno = input("Would you like another garnish? "           
                              "('Y' for yes, 'N' for no)\n: ").upper()
                if yesno == "N":
                    garnishrepeat = 1
                    yesnorepeat = 1
                elif yesno == "Y":
                     yesnorepeat = 1
                else:
                    print("Please Enter 'Y' for yes or 'N' for no.")
        elif garnish == "C":
            price += 2.50
            list.append("Cheese")
            while yesnorepeat == 0:
                yesno = input("Would you like another garnish? "           
                              "('Y' for yes, 'N' for no)\n: ").upper()
                if yesno == "N":
                    garnishrepeat = 1
                    yesnorepeat = 1
                elif yesno == "Y":
                     yesnorepeat = 1
                else:
                    print("Please Enter 'Y' for yes or 'N' for no.")
        else:
            print("Please enter either 'O' for Onion, 'T' for Tomato,"
                  " 'L' for Lettuce, or 'C' for Cheese.")
    return price, list


def breadfunction():
    breadtitle = ""
    breadrepeat = 0
    breadprice = 0
    while breadrepeat != 1:
        bread = input("What kind of bread would you like to order? "
                      "\nWholemeal     $1.00 (press 'M')"
                      "\nWhite         $0.80 (press 'W')"
                      "\nCheesy White  $1.20 (press 'C')"
                      "\nGluten Free   $1.40 (press 'G')"
                      "\n: ").upper()
        if bread == "M":
            breadprice = 1.00
            breadtitle = "Wholemeal"
            breadrepeat = 1
        elif bread == "W":
            breadprice = 0.80
            breadtitle = "White"
            breadrepeat = 1
        elif bread == "C":
            breadprice = 1.20
            breadtitle = "Cheesy White"
            breadrepeat = 1
        elif bread == "G":
            breadprice = 1.40
            breadtitle = "Gluten Free"
            breadrepeat = 1
        else:
            print("Please enter either 'M' for Wholemeal, 'W' for White,"
                  " 'C' for Cheesy White, or 'G' for Gluten free.")
    return breadtitle, breadprice


def meatfuntion():
    meattitle = ""
    meatrepeat = 0
    meatprice = 0
    while meatrepeat != 1:
        meat = input("What kind of meat would you like in your sandwich?"
                     "\nChicken        $2.69 (press 'C')"
                     "\nBeef           $3.00 (press 'B')"
                     "\nSalami         $4.00 (press 'S')"
                     "\nVegan Slice    $3.30 (press 'V')"
                     "\n: ").upper()
        if meat == "C":
            meatprice = 2.69
            meattitle = "Chicken"
            meatrepeat = 1
        elif meat == "B":
            meatprice = 3.00
            meattitle = "Beef"
            meatrepeat = 1
        elif meat == "S":
            meatprice = 4.00
            meattitle = "Salami"
            meatrepeat = 1
        elif meat == "V":
            meatprice = 3.30
            meattitle = "Vegan Slice"
            meatrepeat = 1
        else:
            print("Please enter either 'C' for Chicken, 'B' for Beef,"
                  " 'S' for Salami, or 'V' for Vegan Slice.")
    return meattitle, meatprice

cost = 0

breadreturnfunction = breadfunction()
breadtitle = breadreturnfunction[0]
breadprice = breadreturnfunction[1]
cost += breadprice

meatreturnfunction = meatfuntion()
meattitle = meatreturnfunction[0]
meatprice = meatreturnfunction[1]
cost += meatprice

garnishlist = []
garnishcostlist = []
repeat = 0
garnishreturnfunction = garnishfunction(garnishlist)
garnishlist = garnishreturnfunction[1]
cost += garnishreturnfunction[0]
garnishcost = garnishreturnfunction[0]
garnishlength = len(garnishlist)

while repeat != garnishlength:
    if garnishlist[repeat] == "Onion":
        garnishcostlist.append(1.69)
        repeat += 1
    elif garnishlist[repeat] == "Tomato":
        garnishcostlist.append(1.00)
        repeat += 1
    elif garnishlist[repeat] == "Lettuce":
        garnishcostlist.append(2.00)
        repeat += 1
    elif garnishlist[repeat] == "Cheese":
        garnishcostlist.append(2.50)
        repeat += 1

repeat = 0
print()
print("------------------------------------------")
print()
print(f"Your current order is:\nBread Type:    {breadtitle}----${breadprice}"
      f"\nMeat Type:     {meattitle}----${meatprice}\nGarnish Types: "
      f"{garnishlist[0]}----${garnishcostlist[0]}")
if garnishlength > 1:
    while repeat+1 != garnishlength:
        print(f"               {garnishlist[repeat+1]}----$"
              f"{garnishcostlist[repeat+1]}")
        repeat += 1
print()
print(f"Your total is ${cost}")
confirm = 0
while confirm == 0:
    change = input("Would you like to confirm or change your order?\nPress 'C'"
                   " to Confirm, or 'M' to Make a Change \n: ").upper()
    if change == "C" or "M":
        confirm += 1
    else:
        print("Please press 'C' to Confirm or 'M' to Make a Change.")
while change == 'M':
    changetype = input("Would you like to change the bread, meat, or "
                       "garnishes?\nPress 'B' for Bread, 'M' for Meat, and 'G'"
                       " for Garnishes\n: ").upper()
    if changetype == "G":
        cost -= garnishcost
        garnishlist = []
        garnishcostlist = []
        repeat = 0
        print("Please re-enter all your garnishes:")
        garnishreturnfunction = garnishfunction(garnishlist)
        garnishlist = garnishreturnfunction[1]
        cost += garnishreturnfunction[0]
        garnishcost = garnishreturnfunction[0]
        garnishlength = len(garnishlist)
        while repeat != garnishlength:
            if garnishlist[repeat] == "Onion":
                garnishcostlist.append(1.69)
                repeat += 1
            elif garnishlist[repeat] == "Tomato":
                garnishcostlist.append(1.00)
                repeat += 1
            elif garnishlist[repeat] == "Lettuce":
                garnishcostlist.append(2.00)
                repeat += 1
            elif garnishlist[repeat] == "Cheese":
                garnishcostlist.append(2.50)
                repeat += 1
    elif changetype == 'B':
        cost -= breadprice
        breadreturnfunction = breadfunction()
        breadtitle = breadreturnfunction[0]
        breadprice = breadreturnfunction[1]
        cost += breadprice
    elif changetype == "M":
        cost -= meatprice
        meatreturnfunction = meatfuntion()
        meattitle = meatreturnfunction[0]
        meatprice = meatreturnfunction[1]
        cost += meatprice
    else:
        print("Please press either 'B' for Bread, 'M' for Meat, and "
              "'G' for Garnishes")
    if changetype == "G" or "B" or "M":
        repeat = 0
        print()
        print("------------------------------------------")
        print()
        print(f"Your current order is:\nBread Type:    "
              f"{breadtitle}----${breadprice}\nMeat Type:     "
              f"{meattitle}----${meatprice}\nGarnish Types: "
              f"{garnishlist[0]}----${garnishcostlist[0]}")
        if garnishlength > 1:
            while repeat+1 != garnishlength:
                print(f"               {garnishlist[repeat+1]}----$"
                      f"{garnishcostlist[repeat+1]}")
                repeat += 1
        print()
        print(f"Your total is ${cost}")
        confirm = 0
        while confirm == 0:
            change = input("Would you like to confirm or change your order?\n"
                           "Press 'C' to Confirm, or 'M' to Make a Change \n: "
                           "").upper()
            if change == "C" or "M":
                confirm += 1
            else:
                print("Please press 'C' to Confirm or 'M' to Make a Change.")

print()
print("------------------------------------------")
print()
print(f"Your confirmed order is:\nBread Type:    {breadtitle}----${breadprice}"
      f"\nMeat Type:     {meattitle}----${meatprice}\nGarnish Types: "
      f"{garnishlist[0]}----${garnishcostlist[0]}")
if garnishlength > 1:
    while repeat+1 != garnishlength:
        print(f"               {garnishlist[repeat+1]}----$"
              f"{garnishcostlist[repeat+1]}")
        repeat += 1
print()
print(f"Your total is ${cost}")
