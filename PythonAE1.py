from ProgramFeatures import Option1, Option2, Option3, Option4, Option5

# Handles menu choice via match case.
def HandleChoice(MenuOption):
    match(MenuOption):
        case 1:
            Option1()
        case 2:
            Option2()
        case 3:
            Option3()
        case 4:
            Option4()
        case 5:
            Option5()
        case 6:
            print("\033[91m" + "Exiting..." + "\033[0m")
            quit()
        # If anything other than numbers 1-6, throw error and restart.
        case _:
            print("\n\n\033[91m" + "Error: " + "\033[0m" + "Invalid Selection Made, Please Try Again!")

# Starts process by providing user with menu options.
def Start():
    print("\n\033[4m" + "Billboard Top 100 Songs Search:" + "\033[0m\n")
    # Gets user response to feed into the match case.
    MenuOption = int(input("Please choose your action to take (in the format of 1-6):\n1) Top 5 Songs By Day\n2) Most Successful Artist\n3) Top 5 Longest Charters\n4) Most Improved Song\n5) Song Search\n6) Exit\n" + "\033[1m" + "\nSelection: " + "\033[1m"))
    HandleChoice(MenuOption)

# Only thing that runs immediately. 
while True:
    Start()