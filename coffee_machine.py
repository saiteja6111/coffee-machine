print("☕️")
Menu = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost" : 3.0
    }
}

start = True
Water = 300
Milk = 200
Coffee = 100
Money = 0

def insert_Coin():
    global quarters,dimes,nickles,pennies,Cost
    quarters = float(input("Enter the no of quaters(coins): "))
    dimes = float(input("Enter the no of dimes(coins): "))
    nickles = float(input("Enter the no of nickles(coins): "))
    pennies = float(input("Enter the no of pennies(coins): "))
    Cost = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    Cost = round(Cost,2)

while start:
    print("Welcome to coffee Machine")
    user_choice = input("What would you like? Enter your choice in numbers \n 1 -> espresso \n 2 -> latte \n 3 -> cappuccino \n: ")
    if user_choice.lower() == "off":
        break
    elif user_choice.lower() == "report":
        print(f"\nWater: {Water}ml")
        print(f"Milk: {Milk}ml")
        print(f"Coffee: {Coffee}g")
        print(f"Money: ${Money}\n")
    elif user_choice.lower() == "1":
        insert_Coin()
        if Cost >= 1.50:
            if Water >= Menu["espresso"]["ingredients"]["water"] and Coffee >= Menu["espresso"]["ingredients"]["coffee"]:
                Water -= Menu["espresso"]["ingredients"]["water"]
                Coffee -= Menu["espresso"]["ingredients"]["coffee"]
            Cost -= 1.50
            if Cost > 0:
                print(f"Here is your change ${round(Cost,2)} Thank you!\n")
            else:
                print("Thank You!\n")
        elif Cost < 1.50:
            print("Sorry that's not enough money\n")
            continue
    elif user_choice.lower() == "2":
        insert_Coin()
        if Cost >= 2.50:
            if Water >= Menu["latte"]["ingredients"]["water"] and Milk >= Menu["latte"]["ingredients"]["milk"] and Coffee >= Menu["latte"]["ingredients"]["coffee"]:
                Water -= Menu["latte"]["ingredients"]["water"]
                Milk -= Menu["latte"]["ingredients"]["milk"]
                Coffee -= Menu["latte"]["ingredients"]["coffee"]
            Cost -= 2.50
            if Cost > 0:
                print(f"Here is your change ${round(Cost,2)} Thank you!\n")
                continue
            else:
                print("Thank You!\n")
                continue
        elif Cost < 2.50:
            print("Sorry that's not enough money\n")
            continue
    
    elif user_choice.lower() == '3':
        insert_Coin()
        if Cost >= 3.00:
            if Water >= Menu["cappuccino"]["ingredients"]["water"] and Milk >= Menu["latte"]["ingredients"]["milk"] and Coffee >= Menu["cappuccino"]["ingredients"]["coffee"]:
                Water -= Menu["cappuccino"]["ingredients"]["water"]
                Milk -= Menu["latte"]["ingredients"]["milk"]
                Coffee -= Menu["cappuccino"]["ingredients"]["coffee"]
            Cost -= 3.00
            if Cost > 0:
                print(f"Here is your change ${round(Cost,2)} Thank you!\n")
                continue
            else:
                print("Thank You!\n")
                continue
        elif Cost < 3.00:
            print("Sorry that's not enough money\n")
            continue

            

