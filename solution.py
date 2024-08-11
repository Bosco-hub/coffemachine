from main import MENU, resources, money
# Prompt for coins
def coins():
    print("Please insert coins:")
    quarter = int(input("How many quarters?"))
    dime = int(input("How many dimes?"))
    nickle = int(input("How many nickles?"))
    pennie = int(input("How many pennies?"))
    return float(quarter*.25 + dime*.10 + nickle*.05 + pennie*.01)

is_on = True
while is_on:
# Prompt for user
    coffe_sel = input(f"What would you like? (espresso/latte/cappuccino):").lower()
    if coffe_sel == "off":
# Turn off this shit
        is_on = False
# Enter "report" report with resources
    elif coffe_sel == "report":
        for r, v in resources.items():
            if r == "coffee":
                print(f"{r.title()} : {v}g")
            else:
                print(f"{r.title()} : {v}ml")
        for m, mm in money.items():
            print(f"{m.title()} : ${mm}")
    else:
# Espresso, check resources and cost
        wat = MENU[coffe_sel]["ingredients"]["water"]
        cof = MENU[coffe_sel]["ingredients"]["coffee"]
        mlk = 0
        if coffe_sel == "latte" or coffe_sel == "cappuccino":
            mlk = MENU[coffe_sel]["ingredients"]["milk"]
        if wat > resources["water"]:
            print("Sorry there is not enough water")
        elif cof > resources["coffee"]:
            print("Sorry there is not enough coffee")
        elif mlk > resources["milk"]:
            print("Sorry there is not enough milk")
        if wat <= resources["water"] and cof <= resources["coffee"] and mlk <= resources["milk"]:
            mon = coins()
            if mon < MENU[coffe_sel]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money["money"] += MENU[coffe_sel]["cost"]
                resources["water"] -= wat
                resources["coffee"] -= cof
                resources["milk"] -= mlk
                rem = mon - MENU["espresso"]["cost"]
                print(f"Here is ${round(rem,3)} dollars in change.")
                print(f"Here is your {coffe_sel}. Enjoy!")
# Latte, check resources and cost





